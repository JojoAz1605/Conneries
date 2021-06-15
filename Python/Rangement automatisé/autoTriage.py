from os import listdir, makedirs, path, getcwd, rename
from os.path import isfile, join, basename

currentPath = path.abspath(getcwd())

listOfFiles = []
dicExtensions = {}

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
    print("Création de la liste des fichiers...")
    for file in listdir(currentPath):
        if isfile(join(currentPath, file)):
            listOfFiles.append(file)

def makeExtensionsDict(filesList: list):
    print("Création du dictionnaire des extensions...")
    for file in filesList:
        extension = findExtension(file)
        if extension not in dicExtensions.keys():
            dicExtensions[extension] = 0

def countExtensions():
    global listOfFiles, dicExtensions
    makeListOfFiles()
    makeExtensionsDict(listOfFiles)

    print("Comptage des fichiers...")
    for file in listOfFiles:
        extension = findExtension(file)
        for key in dicExtensions:
            if extension == key:
                dicExtensions[key] += 1
    print("Voici le nombres de fichiers pour chaque extension:\n", dicExtensions)


def organize():
    global listOfFiles, dicExtensions
    countExtensions()
    print("Création des fichiers de rangement...")
    for extension in dicExtensions:
        try:
            makedirs('output' + '\\' + extension)
        except FileExistsError:
            pass
    print("Déplacement des fichiers...")
    for file in listOfFiles:
        print("Déplacement de: ", file)
        if basename(__file__) != file:
            oldPath = currentPath + '\\' + file
            newPath = currentPath + '\\output' + '\\' + findExtension(file) + '\\' + file
            rename(oldPath, newPath)
        else:
            print("Il s'agit de ce fichier là, rangement impossible pour l'instant.")
    print("Tous les fichiers ont été rangés!")


organize()
