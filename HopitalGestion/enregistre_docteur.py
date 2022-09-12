#ici on va enregistrer un medecin
from clean import clearConsole

def afficherIdentiteDocteur(listeDocteur):
    print(f"\
            Nom : {listeDocteur[1]} {listeDocteur[0]} {listeDocteur[2]}\n\
            Numero Telephone : {listeDocteur[3]}\n\
            Matricule : {listeDocteur[4]}\n\
            Specialisation : {listeDocteur[5]}\n")

def enregistrerDocteur():
    clearConsole()
    print("################################################\n")
    print("##              ENREGISTRER DOCTEURs           ##\n")
    print("################################################\n")
    docteur = []
    
    print("Entrez le nom du docteur\n")
    nomDocteur = input(">> ")
    nomDocteur = nomDocteur.upper()
    docteur.append(nomDocteur)
    
    print("Entrez le prenom du docteur\n")
    prenomDocteur = input(">> ")
    prenomDocteur = prenomDocteur.upper()
    docteur.append(prenomDocteur)
    
    print("Entrez le post-nom du docteur\n")
    postNomDocteur = input(">> ")
    postNomDocteur = postNomDocteur.upper()
    docteur.append(postNomDocteur)
    
    print("Entrez le numero de telephone du docteur\n")
    numDocteur = input(">> ")
    docteur.append(numDocteur)

    print("Entrez le matricule du docteur\n")
    matriculeDocteur = input(">> ")
    docteur.append(matriculeDocteur)
    
    print("Entrez la specialisation du docteur\n")
    specialDocteur = input(">> ")
    docteur.append(specialDocteur)
    return docteur
