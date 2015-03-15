import custom
import shutil
from dirtools import Dir

def dbCheck():
    if Dir(custom.dbPath).hash() != custom.dbHash:
        shutil.copytree(custom.dbPath, custom.dbCopyPath)
        custom.dbHash = Dir(custom.dbCopyPath).hash()
    else:
        pass

dbCheck()