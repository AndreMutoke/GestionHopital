from clean import clearConsole
def numeroDossier(numId):
    clearConsole()
    print("#################################################\n")
    print("##         GENERER NUMERO DOSSIER UNIQUE       ##\n")
    print("#################################################\n")

    print("Entrez d'abord la date(2 fois) suivant le format 02-04-2022 \
pour generer le numero du dossier du Patient\n")
    date = input(">> ")
    partA = date[:2]
    partB = date[3:5]
    partC = date[8:]
    return partA+partB+partC+str(numId)

def genererUnNumeroDossier(numId):
    clearConsole()
    print("#################################################\n")
    print("##         GENERER NUMERO DOSSIER UNIQUE       ##\n")
    print("#################################################\n")

    print("Entrez la date suivant le format 02-04-2022 \
pour generer le numero du dossier du Patient\n")
    date = input(">> ")
    partA = date[:2]
    partB = date[3:5]
    partC = date[8:]
    print(f"Voici comment se presente le numero Dossier\n\
                {partA+partB+partC+str(numId)}\n")
