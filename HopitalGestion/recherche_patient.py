import os
from clean import clearConsole
from enregistre_patient import afficherIdentitePatient

def recherchePatientNom(listePatients, nomPatient):
    for i in range(len(listePatients)):
        if nomPatient == listePatients[i][0]:
            afficherIdentitePatient(listePatients[i])

def recherchePatientPrenom(listePatients, prenomPatient):
    for i in range(len(listePatients)):
        if prenomPatient == listePatients[i][1]:
            afficherIdentitePatient(listePatients[i])

def recherchePatientPostNom(listePatients, postNomPatient):
    for i in range(len(listePatients)):
        if postNomPatient == listePatients[i][2]:
            afficherIdentitePatient(listePatients[i])

def recherchePatientTaille(listePatients, taillePatient):
    for i in range(len(listePatients)):
        if taillePatient == listePatients[i][5]:
            afficherIdentitePatient(listePatients[i])

def recherchePatientAge(listePatients, agePatient):
    for i in range(len(listePatients)):
        if agePatient == listePatients[i][7]:
            afficherIdentitePatient(listePatients[i])
def recherchePatientId(listePatients, numId):
    for i in range(len(listePatients)):
        if numId == listePatients[i][8]:
            afficherIdentitePatient(listePatients[i])

def recherchePatientIdentite(listePatients):
    clearConsole()
    print("################################################\n")
    print("##              RECHERCHE PATIENT             ##\n")
    print("################################################\n")
    if len(listePatients) != 0:
        print("Suivant quoi voulez-vous etablir la recherche ?\
                1. Le Nom\n\
                2. Le prenom\n\
                3. Le post-nom\n\
                4. La taille\n\
                5. L'age\n")
        choiceUser = int(input(">> "))
        while choiceUser<1 or choiceUser>5:
            print("Desole, une erreur est survenue veillez reprendre svp !\n")
            print("Suivant quoi voulez-vous etablir la recherche ?\n\
                    1. Le Nom\n\
                    2. Le prenom\n\
                    3. Le post-nom\n\
                    4. La taille\n\
                    5. L'age\n")
            choiceUser = int(input(">> "))
        if choiceUser==1:
            print("Entrez le nom du patient dont vous cherchez \n")
            nomPatient = input(">> ")
            nomPatient = nomPatient.upper()
            recherchePatientNom(listePatients, nomPatient)
            
        elif choiceUser==2:
            print("Entrez le prenom du patient dont vous cherchez \n")
            prenomPatient = input(">> ")
            prenomPatient = prenomPatient.upper()
            recherchePatientNom(listePatients, prenomPatient)

        elif choiceUser==3:
            print("Entrez le post-nom du patient dont vous cherchez \n")
            postNomPatient = input(">> ")
            postNomPatient = postNomPatient.upper()
            recherchePatientNom(listePatients, postNomPatient)

        elif choiceUser==4:
            print("Entrez la taille du patient dont vous cherchez \n")
            taillePatient = input(">> ")
            taillePatient = taillePatient.upper()
            recherchePatientNom(listePatients, taillePatient)

        else:
            print("Entrez la taille du patient dont vous cherchez \n")
            agePatient = input(">> ")
            agePatient = agePatient.upper()
            recherchePatientNom(listePatients, agePatient)
    else:
        print("Desole il n'y a pas des patients pour l'instant !\n")

def recherchePatientNumeDossier(listePatients):
    clearConsole()
    print("################################################\n")
    print("##              RECHERCHE PATIENT             ##\n")
    print("################################################\n")
    if len(listePatients) != 0 :
        print("Entrez le numero du dossier dont vous cherchez \n")
        numId = input(">> ")
        recherchePatientId(listePatients, numId)

    else:
        print("Desole il n'y a pas des patients pour l'instant !\n")
        



    
