searchPhrase = 'swagger'
replaceWith = None #None or string
# TO DO add NOT_PHRASES

firstPath = "C:/Users/jdqsj/Desktop/ClareAI/Workspace/ClareBot"


## Search filters
EXCLUDES = ["Dependency","node_modules","searchAll.py","Debug"] #None or array, does not search if phrase is found in full path

INVALID_EXTS = None #None or array, does not search file if ext is found in this list

REQUIRED_EXTS = None #None #None or array, when not None, searches files only with at least one ext in list

MUST_HAVE = None #None or array, when not None, only records answer when at least one phrase is found in full path 
# example usage: MUST_HAVE = ["Folder1"], /Folder/Folder1/file1 is eligible, but /Folder/File is not permitted to searched

### IMPORTS
import os
RESULTS = []
RESULTS_UNIQUE = []

def checkFile(path):
    try: #try to open the file (works for text and script files, but not png, video, etc.)
        f = open(path,'r')
        lines = f.readlines()
        for i in range(len(lines)):
            if searchPhrase in lines[i]:
                if validMustHave(path): 
                    if not path in RESULTS_UNIQUE:
                        RESULTS_UNIQUE.append(path)
                    # TO DO, replace that line and write it
                    RESULTS.append("FOUND IN %d:%s"%(i+1,path))
        f.close()
    except Exception as e:
        pass
def validPath(path):
    for exclude in EXCLUDES:
        if exclude in path:
            return False
    return True
def validMustHave(path):
    if MUST_HAVE == None: return True
    for name in MUST_HAVE:
        if name in path: return True
    return False
def validExt(fname):
    if INVALID_EXTS != None:
        for ext in INVALID_EXTS:
            if fname.endswith(ext):
                return False
    if REQUIRED_EXTS == None: return True
    else:
        for ext in REQUIRED_EXTS:
            if fname.endswith(ext):
                return True
        
    return False
def checkFiles(mainPath):
    for fname in os.listdir(mainPath):
        newPath = mainPath + "/" + fname
        if not validPath(newPath): continue #skip excluded paths
        if os.path.isdir(newPath):
            checkFiles(newPath)
        else:
            if not validExt(fname): continue #skip invalid exts
            checkFile(newPath)


checkFiles(firstPath)

for line in RESULTS_UNIQUE:
    print(line.replace("C:/Users/jdqsj/Desktop/ClareAI/Workspace/",""))
