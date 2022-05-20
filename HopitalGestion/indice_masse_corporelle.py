from clean import clearConsole
def afficherIMCPatient(listePatients, numId):
    clearConsole()
    print("#################################################\n")
    print("##           INDICE DE MASSE CORPOREL          ##\n")
    print("#################################################\n")
    if(len(listePatients) != 0):
        for i in range(len(listePatients)):
            if(listePatients[i][8] == numId):
                poids = float(listePatients[i][4])
                taille = float(listePatients[i][5])
                imc = poids/(taille**2)
                diagnostique = ""
                if imc < 18.5:
                    diagnostique = "INSUFFISANCE PONDERALE (MAIGREUR)"
                elif imc >=18.5 and imc<25:
                    diagnostique = "CORPULANCE NORMALE"
                elif imc >=25 and imc<30:
                    diagnostique = "SURPOIDS"
                elif imc >=30 and imc<35:
                    diagnostique = "OBESITE MODEREE"
                elif imc >=35 and imc<40:
                    diagnostique = "OBESITE SEVERE"
                elif imc >=40:
                    diagnostique = "OBESITE MORBITE (MASSIVE)"
                else:
                    print("RAS")
                print(f"Nom : {listePatients[i][1]} {listePatients[i][0]} {listePatients[i][2]}\n\
                        Poids : {listePatients[i][4]}\n\
                        Taille : {listePatients[i][5]}\n\
                        Indice de Masse Corporelle : {imc}\n\
                        Diagnostique : {diagnostique }\n")

    else:
        print("Desole, il n'y a pas encore des patients !\n")