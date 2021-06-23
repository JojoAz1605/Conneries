from os import listdir, path, getcwd, remove
from os.path import isfile, join

depart = path.abspath(getcwd()) + "\\ayo"
extensionCount = {"dossiers": 1}

def getDirName(directory: str):
    index = len(directory) + 1
    name = ''
    for letter in reversed(directory):
        index -= 1
        if str(letter) == '\\':
            break
    for letter in range(index, len(directory)):
        name += directory[letter]
    return name


def indexOf(string: str, val: str):
    for elem in range(len(string)):
        if val == string[elem]:
            return elem
    return False


def findExtension(fileName: str):
    extension = ''
    pointIndex = indexOf(fileName, '.')
    for i in range(pointIndex + 1, len(fileName)):
        extension += fileName[i]
    return extension


class Dossier:
    def __init__(self, directory):
        self.dir = directory
        self.name = getDirName(self.dir)
        self.writeLog("Initialisation...")

        self.folders = []
        self.files = []

        self.listAll()

    def listAll(self):
        global extensionCount
        self.writeLog("Création des listes...")
        try:
            for elem in listdir(self.dir):
                try:
                    if isfile(join(self.dir, elem)):
                        extension = findExtension(elem)
                        self.writeLog("Fichier trouvé: " + elem)
                        self.files.append(elem)
                        try:
                            extensionCount[extension] += 1
                        except KeyError:
                            extensionCount[extension] = 1
                    else:
                        self.writeLog("Dossier trouvé: " + elem)
                        self.folders.append(Dossier(self.dir + '\\' + elem))
                        extensionCount["dossiers"] += 1
                except PermissionError:
                    pass
                except UnicodeEncodeError:
                    pass
        except NotADirectoryError:
            pass

    def writeLog(self, string: str):
        logFile = open("log.txt", 'a')
        print(self.dir + " - " + str(string))
        logFile.write(self.dir + " - " + str(string) + "\n")
        logFile.close()

    def writeResults(self, res: list, rech: str):
        self.writeLog("écriture des résultats pour la recherche \"" + rech + "\"...")
        resFile = open("search results -" + rech + "-.txt", 'a')
        for elem in res:
            if elem is not None:
                resFile.write("\n" + str(elem) + '\n')
        resFile.close()

    def search(self, rech: str):
        match = []
        for folder in self.folders:
            match.append(folder.search(rech))
            for file in folder.files:
                if rech in file:
                    match.append(file)
            if rech in folder.name:
                match.append((folder.name, folder.dir))
        self.writeResults(match, rech)

    def suppressionDesFichiers(self, active: bool):
        """
        A utiliser à vos risques et périls
        CETTE FONCTION EST DANGEREUSE, NE L'UTILISEZ SURTOUT PAS
        A PARTIR DE LA RACINE DE VOTRE DISQUE
        """
        self.writeLog("SUPPRESSION DES FICHIERS ENCLENCHEE")
        if active:
            for folder in self.folders:
                folder.suppressionDesFichiers(True)
                for file in self.files:
                    self.writeLog("Suppression du fichier: " + file)
                    remove(self.dir + "\\" + file)


thisFolder = Dossier(path.abspath(depart))
thisFolder.search("un")

extensionFile = open("extension count.txt", 'w')
extensionFile.write(str(extensionCount))
extensionFile.close()

thisFolder.suppressionDesFichiers(False)  # Ne mettre sur True que si vous savez ce que vous faites
