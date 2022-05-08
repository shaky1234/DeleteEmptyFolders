#To find Empty Folders and Delete them
#Does not do rescursive yet
from os import listdir, walk, rmdir

#Your starting directory
startpath = "D:\\Norp\\Movies\\Reddit"

class dirObj:
    def __init__(self, DirPath, DirName):
        self.DirPath = DirPath
        self.DirName = DirName
        

dirlist = []
for (dirpath, dirname, filenames) in walk(startpath):
    for d in dirname:dirlist.append(dirObj(dirpath,d))


for q in dirlist: 
    if not listdir("{}\\{}".format(q.DirPath, q.DirName)):
        rmdir("{}\\{}".format(q.DirPath, q.DirName))