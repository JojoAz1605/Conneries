from os import listdir, makedirs, path, getcwd, rename
from os.path import isfile, join, basename

depart = path.abspath(getcwd()) + "\\unDossier"

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

class Dossier:
    def __init__(self, directory):
        self.dir = directory
        self.name = getDirName(self.dir)
        self.writeLog("Initialisation...")

        self.folders = []
        self.files = []

        self.listAll()

    def listAll(self):
        self.writeLog("Création des listes...")
        for elem in listdir(self.dir):
            try:
                if isfile(join(self.dir, elem)):
                    self.writeLog("Fichier trouvé: " + elem)
                    self.files.append(elem)
                else:
                    self.writeLog("Dossier trouvé: " + elem)
                    self.folders.append(Dossier(self.dir + '\\' + elem))
            except PermissionError:
                pass
            except UnicodeEncodeError:
                pass

    def writeLog(self, string: str):
        logFile = open("log.txt", 'a')
        print(self.dir + " - " + str(string))
        logFile.write(self.dir + " - " + str(string) + "\n")
        logFile.close()

    def search(self, string: str):
        match = []
        for folder in self.folders:
            match.append(''.join(folder.search(string)))
            for file in folder.files:
                if string in file:
                    match.append(file)
            if string in folder.name:
                match.append(folder.dir)
        self.writeLog(match)
        return match


thisFolder = Dossier(path.abspath(depart))
print(thisFolder.search("un"))
