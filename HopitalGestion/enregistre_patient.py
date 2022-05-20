from clean import clearConsole

def afficherIdentitePatient(listePatient):
    print(f"\
            Nom : {listePatient[1]} {listePatient[0]} {listePatient[2]}\n\
            Age : {listePatient[7]} ans\n\
            Genre : {listePatient[6]}\n\
            Poids : {listePatient[4]} Kg\n\
            Taille : {listePatient[5]} metre(s)\n\
            Numero de Telephone : {listePatient[3]}\n\
            Numero Dossier : {listePatient[8]}\n")

def enregistrerPatient(numId):
    clearConsole()
    print("################################################\n")
    print("##              ENREGISTRER PATIENT           ##\n")
    print("################################################\n")
    patient = []

    print("Entrez le nom du patient\n")
    nomPatient = input(">> ")
    nomPatient = nomPatient.upper()
    patient.append(nomPatient)

    print("Entrez le Prenom du patient\n")
    prenomPatient = input(">> ")
    prenomPatient = prenomPatient.upper()
    patient.append(prenomPatient)

    print("Entrez le post-nom du patient\n")
    postNomPatient = input(">> ")
    postNomPatient = postNomPatient.upper()
    patient.append(postNomPatient)

    print("Entrez le numero de telephone du patient\n")
    numPatient = input(">> ")
    patient.append(numPatient)

    print("Entrez le poids du patient en Kg\n")
    poidsPatient = float(input(">> "))
    patient.append(poidsPatient)

    print("Entrez la taille du patient en m\n")
    taillePatient = float(input(">> "))
    patient.append(taillePatient)

    print("Entrez le Genre du patient(M/F)\n")
    genrePatient = input(">> ")
    genrePatient = genrePatient.upper()
    patient.append(genrePatient)

    print("Entrez l'age du patient\n")
    agePatient = int(input(">> "))
    patient.append(agePatient)

    patient.append(numId)

    return patient

def enregistrerPlaintePatient(listePatients, numId):
    if len(listePatients)!=0:
        for i in range(len(listePatients)):
            if numId == listePatients[i][8]:
                print("Entrez votre plainte !\n")
                plainte = input(">> ")
                listePatients[i].append(plainte)
    else:
        print("Desole il n'y a pas des patients pour l'instant !\n")

def afficherPlaintePatientSelonNumUnique(listePatients, numId):
    if len(listePatients)!=0:
        for i in range(len(listePatients)):
            if numId == listePatients[i][8]:
                if len(listePatients[i])==10:
                    print(listePatients[i][-1])
                    print("\n *****************FIN DE L'OPERATION***************\n")
                else:
                    for j in range(9, len(listePatients[i])):
                        print(listePatients[i][j])
                        print("\n")
                    print("\n *****************FIN DE L'OPERATION***************\n")



















                        
    else:
        print("Desole il n'y a pas des patients pour l'instant !\n")




