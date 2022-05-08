from os import listdir, walk

#Your starting directory
startpath = "C:\\Users\\guest\\Pictures"

class dirObj:
    def __init__(self, DirPath, DirName):
        self.DirPath = DirPath
        self.DirName = DirName
        

dirlist = []
for (dirpath, dirname, filenames) in walk(startpath):
    for d in dirname:dirlist.append(dirObj(dirpath,d))


for q in dirlist: 
    if not listdir("{}\\{}".format(q.DirPath, q.DirName)):
        print("{} It's Empty".format("{}\\{}".format(q.DirPath, q.DirName)))
    else:
        print("{} There are Files".format("{}\\{}".format(q.DirPath, q.DirName)))