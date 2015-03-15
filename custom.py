import os
from dirtools import Dir

dbPath = 'Network/sigDB.db'
dbCopyPath = 'sigDBCopied.db'
if os.path.isdir(dbCopyPath):
    dbHash = Dir((dbCopyPath).hash())
else:
    dbHash = 0

