listeMots = []  # stocke tous les mots
listeMotsPourCalculs = []


def plusGrandNbAnagrammes():
    """Calcul le nombre d'anagrammes(d'un mot) pour chaque mot

    :return: le mot possédant le plus grand nombre d'anagrammes(tuple)
    """
    plusGrand = {
        "mot": '',
        "nbAnagrammes": 0,
        "anagrammes": []
    }
    creationListeMots()
    cp = 0  # sert de compteur

    for mot in listeMotsPourCalculs:
        nbAnagrammes = len(donneAnagrammes(normalize(mot), listeMotsPourCalculs))  # défini le nb d'anagrammes d'un mot
        print(cp, round((cp * 100) / len(listeMotsPourCalculs), 2), "%", "|", plusGrand, '| Mot actuel: ', normalize(mot))  # affichage
        # si le nb d'anagrammes du mot est plus grand que l'ancien, le remplace
        if nbAnagrammes > plusGrand["nbAnagrammes"]:
            plusGrand["mot"] = lisible(mot)
            plusGrand["nbAnagrammes"] = nbAnagrammes
            plusGrand["anagrammes"] = donneAnagrammes(mot, listeMots)
        cp += 1  # incrémente le compteur
    return plusGrand


def donneAnagrammes(mot, listeDeMot):
    """Retourne les anagrammes pour un mot

    :param mot: explicite/20(str)
    :param listeDeMot: une liste de référence(list)
    :return: une liste des anagrammes(list)
    """
    global listeMotsPourCalculs
    listeAnagrammes = []  # stocke les anagrammes trouvés
    for unMot in listeDeMot:
        # check si les deux mots sont de la même taille, et si ils sont composés des mêmes lettres
        if len(normalize(mot)) == len(normalize(unMot)) and memeLettres(list(normalize(mot)), list(normalize(unMot))):
            listeAnagrammes.append(lisible(unMot))  # ajoute l'anagramme à la liste
            try:
                listeMotsPourCalculs.remove(unMot)  # retire l'anagramme trouvé dans la liste des mots
            except ValueError:
                pass
    return listeAnagrammes


def compteLettres(liste):
    """Compte les lettres d'une liste de lettres

    :param liste: liste contenant des lettres(list)
    :return: un dico du nombre de lettres(dict)
    """
    dico = {}
    for lettre in liste:
        try:
            dico[lettre] += 1
        except KeyError:  # Si la clé n'existe pas, la créer
            dico[lettre] = 1
    return dico


def memeLettres(liste1, liste2):
    """Vérifie que deux liste de lettres sont les mêmes

    :param liste1: liste de lettre(list)
    :param liste2: liste de lettre(list)
    :return: vrai ou faux(bool)
    """
    if compteLettres(liste1) == compteLettres(liste2):
        return True
    else:
        return False


def normalize(mot):  # permet de normaliser la forme du mot, les accents, caractères spéciaux, etc...
    mot = mot.lower()  # passe le mot en minuscule
    newMot = ''  # permet de stocker le nouveau mot
    for lettre in mot:  # pour chaque lettre dans le mot
        # assez explicite
        if lettre in '\n-)!\'.':
            newMot += ''
        elif lettre == 'œ':
            newMot += "oe"
        elif lettre in 'éèêë':
            newMot += 'e'
        elif lettre in 'îï':
            newMot += 'i'
        elif lettre in 'âàä':
            newMot += 'a'
        elif lettre == 'ç':
            newMot += 'c'
        elif lettre == 'ô':
            newMot += 'o'
        elif lettre in 'ùûü':
            newMot += 'u'
        else:
            newMot += lettre  # ajoute la lettre telle quelle
    return newMot  # retourne le mot


def creationListeMots():  # Permet de créer la liste de mots en lisant un txt
    global listeMots, listeMotsPourCalculs
    txtMots = open("liste_francais.txt", 'r')  # Ouvre le fichier txt
    lignes = txtMots.readlines()  # lit toutes les lignes et les stocke dans une variable
    for mot in lignes:  # pour chaque mot existant dans lignes
        listeMots.append(mot)  # l'ajoute à la liste de mot
    txtMots.close()  # ferme le txt
    # retire les expressions
    for mot in listeMots:
        if mot in " -":
            listeMots.remove(mot)
    listeMotsPourCalculs = listeMots.copy()


def lisible(mot):
    newMot = ''
    for lettre in mot:
        if lettre in '\n':
            newMot += ''
        else:
            newMot += lettre
    return newMot


def main():
    plusGrandNbAnagrammes()


main()

# pause du programme quand lancé via le cmd
while True:
    pass
