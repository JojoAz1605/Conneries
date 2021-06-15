from os import listdir, makedirs, path, getcwd, rename
from os.path import isfile, join, basename

currentPath = path.abspath(getcwd())

listOfFiles = []
dicExtensions = {}
exceptions = [basename(__file__), "log.txt"]

def writeLog(string: str):
    logFile = open("log.txt", 'a')
    print(string)
    logFile.write(string + "\n")
    logFile.close()

def indexOf(string: str, val: str):
    for elem in range(len(string)):
        if val == string[elem]:
            return elem
    return False

def findExtension(fileName: str):
    extension = ''
    pointIndex = indexOf(fileName, '.')
    for i in range(pointIndex+1, len(fileName)):
        extension += fileName[i]
    return extension

def makeListOfFiles():
    global currentPath
    writeLog("Création de la liste des fichiers...")
    for file in listdir(currentPath):
        if isfile(join(currentPath, file)):
            listOfFiles.append(file)

def makeExtensionsDict(filesList: list):
    writeLog("Création du dictionnaire des extensions...")
    for file in filesList:
        extension = findExtension(file)
        if extension not in dicExtensions.keys():
            dicExtensions[extension] = 0

def countExtensions():
    global listOfFiles, dicExtensions
    makeListOfFiles()
    makeExtensionsDict(listOfFiles)
    writeLog("Comptage des fichiers...")
    for file in listOfFiles:
        extension = findExtension(file)
        for key in dicExtensions:
            if extension == key:
                dicExtensions[key] += 1
    writeLog("Voici le nombres de fichiers pour chaque extension:\n" + str(dicExtensions))


def organize():
    global listOfFiles, dicExtensions
    countExtensions()
    writeLog("Création des fichiers de rangement...")
    for extension in dicExtensions:
        try:
            makedirs('output' + '\\' + extension)
        except FileExistsError:
            pass
    writeLog("Déplacement des fichiers...")
    for file in listOfFiles:
        writeLog("Déplacement de: " + file)
        if file in exceptions:
            writeLog("Impossible de déplacer ce fichier là pour l'instant.")
        else:
            oldPath = currentPath + '\\' + file
            newPath = currentPath + '\\output' + '\\' + findExtension(file) + '\\' + file
            rename(oldPath, newPath)
    writeLog("Tous les fichiers ont été rangés!")


organize()

while True:
    pass
