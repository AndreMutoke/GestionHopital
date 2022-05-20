import os
from enregistre_docteur import *
from enregistre_patient import *
from genere_numero_dossier import *
from recherche_patient import *
from enregistre_horaire_docteur import *
from indice_masse_corporelle import *
from clean import clearConsole

#Declaration des variables globales
listeDocteurs=[]
listePatients=[]
numeroDossiers=[]
listeHoraire=[]

def enregistrePlaintePatient():
    clearConsole()
    print("################################################\n")
    print("##            ENREGISTRER PLAINTES            ##\n")
    print("################################################\n")
    print("Veuillez entrer le numero de dossier du patient \n")
    numId = input(">> ")
    enregistrerPlaintePatient(listePatients, numId)

def affichePlaintePatientSelonNumUnique():
    clearConsole()
    print("################################################\n")
    print("##         AFFICHER PLAINTES PATIENTS         ##\n")
    print("################################################\n")
    print("Veuillez entrer le numero de dossier du patient \n")
    numId = input(">> ")
    afficherPlaintePatientSelonNumUnique(listePatients, numId)


def genererNumeroDossier():
    numeroDossiers.append(numeroDossier(len(listePatients)+1))
    return numeroDossier(len(listePatients)+1)
    

def afficherDocteurs():
    clearConsole()
    print("################################################\n")
    print("##              LISTE DES DOCTEURS            ##\n")
    print("################################################\n")
    taille = len(listeDocteurs)
    if taille != 0:
        for i in range(taille):
            afficherIdentiteDocteur(listeDocteurs[i])
    else :
        print("Desole Aucun Docteur n'est enregistrer pour le moment ! \n")

def verifierDisponibiliteDocteur():
    clearConsole()
    print("################################################\n")
    print("##       VERIFIER DISPONIBILITE DOCTEUR       ##\n")
    print("################################################\n")
    print("Faites votre choix :\n")
    print("\
            1.AFFICHER PROGRAMME DOCTEUR\n\
            2.PLANIFIER RENDEZ-VOUS AVEC DOCTEUR\n")
    choix = int(input(">> "))
    while(choix!=1 and choix!=2):
        clearConsole()
        print("################################################\n")
        print("##       VERIFIER DISPONIBILITE DOCTEUR       ##\n")
        print("################################################\n")
        print("un probleme est survenue reesayer svp !\n")
        print("Faites votre choix :\n")
        print("\
                1.AFFICHER PROGRAMME DOCTEUR\n\
                2.PLANIFIER RENDEZ-VOUS AVEC DOCTEUR\n")
        choix = int(input(">> "))
    if choix==1:
        afficherHoraireDocteur(listeDocteurs)
    else:
        print("Entrez le nom du docteur\n")
        nom = input(">> ")
        nom = nom.upper()
        print("Entrez le prenom du docteur\n")
        prenom = input(">> ")
        prenom = prenom.upper()
        print("Entrez le post-nom du docteur\n")
        postNom = input(">> ")
        postNom = postNom.upper()
        print("Entrez le jour du Rendez-vous\n")
        jour = input(">> ")
        jour = jour.upper()
        print("Entrez la ieme heure du Rendez-vous\n")
        heure =int(input(">> "))        
        planifierHoraireDocteur(listeDocteurs, nom, prenom, postNom, jour, heure)

def afficherPatients():
    clearConsole()
    print("################################################\n")
    print("##              LISTE DES PATIENTS            ##\n")
    print("################################################\n")
    taille = len(listePatients)
    if taille != 0:
        for i in range(taille):
            afficherIdentitePatient(listePatients[i])
    else :
        print("Desole Aucun Patient n'est enregistrer pour le moment ! \n")
    
def afficheIMCPatient():
    print("Entrez le numero du dossier\n")
    numId = input(">> ")
    
    afficherIMCPatient(listePatients, numId)

def menu():
    print("################################################\n")
    print("##                    MENU                    ##\n")
    print("################################################\n")
    print("\
          1.ENREGISTRER UN DOCTEUR\n\
          2.ENREGISTRER UN PATIENT\n\
          3.GENERER UN NUMERO DE DOSSIER\n\
          4.CHERCHER UN PATIENT PAR SON IDENTITE\n\
          5.CHERCHER UN PATIENT PAR SON NUMERO DOSSIER\n\
          6.AFFICHER TOUT LES PATIENTS\n\
          7.AFFICHER TOUT LES DOCTEURS\n\
          8.ENREGISTRE PLAINTES D'UN PATIENT\n\
          9.ENREGISTRER L'HORAIRE DE CHAQUE DOCTEUR\n\
          10.VERIFIER LA DISPONIBILITE DU DOCTEUR\n\
          11.AFFICHER LES PLAINTES DU PATIENT SUIVANT SON NUMERO UNIQUE\n\
          12.AFFICHER IMC(Indice de Masse Corporel)\n\
          0. Quitter\n")
    option = int(input(">> "))
    while(option<0 or option>12):
        clearConsole()
        print("Desole votre selection n'est pas reconnue, veuillez reesayer svp!!!\n")
        print("\
          1.ENREGISTRER UN DOCTEUR\n\
          2.ENREGISTRER UN PATIENT\n\
          3.GENERER UN NUMERO DE DOSSIER\n\
          4.CHERCHER UN PATIENT PAR SON IDENTITE\n\
          5.CHERCHER UN PATIENT PAR SON NUMERO DOSSIER\n\
          6.AFFICHER TOUT LES PATIENTS\n\
          7.AFFICHER TOUT LES DOCTEURS\n\
          8.ENREGISTRE PLAINTES D'UN PATIENT\n\
          9.ENREGISTRER L'HORAIRE DE CHAQUE DOCTEUR\n\
          10.VERIFIER LA DISPONIBILITE DU DOCTEUR\n\
          11.AFFICHER LES PLAINTES DU PATIENT SUIVANT SON NUMERO UNIQUE\n\
          12.AFFICHER IMC(Indice de Masse Corporel)\n\
          0. Quitter\n")
        option = int(input(">> "))
    selectOption(option)
def selectOption(option):
    if option==1:
        listeDocteurs.append(enregistrerDocteur())
        os.system('pause')
        clearConsole()
        menu()
    elif option==2:
        listePatients.append(enregistrerPatient(genererNumeroDossier()))
        os.system('pause')
        clearConsole()
        menu()
    elif option==3:
        genererUnNumeroDossier(len(listePatients)+1)
        os.system('pause')
        clearConsole()
        menu()
    elif option==4:
        recherchePatientIdentite(listePatients)
        os.system('pause')
        clearConsole()
        menu()
    elif option==5:
        recherchePatientNumeDossier(listePatients)
        os.system('pause')
        clearConsole()
        menu()
    elif option==6:
        afficherPatients()
        os.system('pause')
        clearConsole()
        menu()
    elif option==7:
        afficherDocteurs()
        os.system('pause')
        clearConsole()
        menu()
    elif option==8:
        enregistrePlaintePatient()
        os.system('pause')
        clearConsole()
        menu()
    elif option==9:
        enregistrerHoraireDocteur(listeDocteurs)
        os.system('pause')
        clearConsole()
        menu()

    elif option==10:
        verifierDisponibiliteDocteur()
        os.system('pause')
        clearConsole()
        menu()
    
    elif option==11:
        affichePlaintePatientSelonNumUnique()
        os.system('pause')
        clearConsole()
        menu()
    elif option==12:
        afficheIMCPatient()
        os.system('pause')
        clearConsole()
        menu()
    else :
        return
    
def main():
    menu()
