from clean import clearConsole
jours = ["LUNDI",
         "MARDI",
         "MERCREDI",
         "JEUDI",
         "VENDREDI",
         "SAMEDI",
         "DIMANCHE"]
heureTravail = ["08h - 09h",
                "09h - 10h",
                "10h - 11h",
                "11h - 12h",
                "12h - 13h",
                "13h - 14h",
                "14h - 15h",
                "15h - 16h",
                "16h - 17h"]

def afficherHoraireDocteur(listeDocteurs):
    clearConsole()
    print("################################################\n")
    print("##        ENREGISTRER HORAIRE DOCTEURS        ##\n")
    print("################################################\n")
    
    if (len(listeDocteurs) != 0):
        for i in range(len(listeDocteurs)):
            print(f"Docteur : {listeDocteurs[i][1]} {listeDocteurs[i][0]} {listeDocteurs[i][2]}\n")
            for j in range(len(jours)):
                print(f"\t{jours[j]} :\n")
                for k in range(len(heureTravail)):
                    print(f"\t\t{k+1}e heure : {listeDocteurs[i][6][j][k]}\n")
                    
    else:
        print("Desole il n'y a pas des docteurs pour l'instant ou pas d'horaire\n")
def planifierHoraireDocteur(listeDocteurs, nom, prenom, postNom, jour, heure):
    clearConsole()
    print("################################################\n")
    print("##        ENREGISTRER HORAIRE DOCTEURS        ##\n")
    print("################################################\n")
    if len(listeDocteurs)!=0 :
        for i in range(len(listeDocteurs)):
            if ((listeDocteurs[i][0] == nom) and (listeDocteurs[i][1] == prenom) and (listeDocteurs[i][2] == postNom)):
                for j in range(7):
                    if jour == jours[j]:
                        if listeDocteurs[i][6][j][heure-1] != "":
                            print(f"Desole a cette heure le docteur {listeDocteurs[i][1]} {listeDocteurs[i][0]} {listeDocteurs[i][2]} est occupe\n")
                        else :
                            print("Entrez votre nom")
                            nomUser = input(">> ")
                            nomUser = nomUser.upper()
                            msg = "RDV AVEC "+nomUser
                            listeDocteurs[i][6][j][heure-1] = msg
    else:
        print("Desole il n'y a pas des docteurs pour l'instant ou pas d'horaire\n")
    


def enregistrerHoraireDocteur(listeDocteurs):
    clearConsole()
    print("################################################\n")
    print("##        ENREGISTRER HORAIRE DOCTEURS        ##\n")
    print("################################################\n")
    
    listeJoursTravail = []
    listeHeureTravail = []
    programme = ""
    if len(listeDocteurs) != 0:
        #Pour chaque Docteur de la liste
        for i in range(len(listeDocteurs)):
                       
            for j in range(len(jours)):
                
                print(f"{jours[j]} :\n")                
                for k in range(len(heureTravail)):
                    print(f"{k+1}e heure ({heureTravail[k]}) :\n")
                    programme = input(">> ")
                    programme = programme.upper()
                    listeHeureTravail.append(programme)
                listeJoursTravail.append(listeHeureTravail)
                listeHeureTravail = []
            listeDocteurs[i].append(listeJoursTravail)
            listeJoursTravail = []
            
            
            
    else:
        print("Desole il n'y a pas des docteurs pour l'instant\n")
