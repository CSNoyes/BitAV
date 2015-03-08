import unittest
import sys
import os

suiteString = """
def suite():
    test_suite = unittest.TestSuite()
    {s}
    return test_suite
"""

def getTestNames():
    def capitalize(str):
        return str[:1].upper() + str[1:]
    # directory walker
    db = {}
    for dirname, dirnames, filenames in os.walk('.'): 
        newDirName = "" if os.path.basename(dirname) == '.' else os.path.basename(dirname) + "."
        for filename in filenames:
            if filename.startswith("__"): continue
            if filename.endswith("pyc"): continue
            if filename == "testAll.py": continue
            filenameWithoutExtension = os.path.splitext(filename)[0]
            capitalizedFileName = capitalize(filenameWithoutExtension)
            fromName = newDirName + filenameWithoutExtension            
            db[capitalizedFileName] = fromName

    importString = ""
    test_suiteString = ""
    for (key, value) in db.items():
        importString += "from %s import %s\n" % (value, key)
        test_suiteString += "test_suite.addTest(unittest.makeSuite(%s))\n    " % key
        
    generated_code = "%s\n%s" % (importString, suiteString.format(s = test_suiteString))
    return generated_code

if __name__ == "__main__":
    sys.path.append("../src")
    sys.path.append("../src/core")

    print getTestNames()
    exec(getTestNames())

    unittest.TextTestRunner(verbosity=2).run(suite())
    
    