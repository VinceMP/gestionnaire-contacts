import json
contacts = []

def afficher_contact(information):
       print ("Nom ", information["nom"])
       print ("Prenom ", information["prenom"])
       print ("E-Mail" , information["mail"])

try:
    with open("contacts.json", "r") as fichier:
        contacts = json.load(fichier)
except:
    contacts = []
while True:
    try:
        chiffre = int(input("Taper 1 pour ajouter un contact\n Taper 2 pour afficher les contacts\n Taper 3 pour quitter "))
        
    except:
        print("Taper l'un des numéros demandé")
        continue
    if   chiffre == 1:
     
        nom = str(input("taper votre nom "))
        prenom = str(input("tapez votre Prenom "))
        mail = input("Taper votre E-mail ")

        contact = {"nom": nom, "prenom": prenom, "mail": mail}
        contacts.append(contact)
        with open("contacts.json", "w") as fichier:
           json.dump(contacts, fichier)
        print("Contacte ajouté ")


    elif chiffre == 2:
       if contacts:
              for contact in contacts:
                  afficher_contact(contact)
       else:
           print("La liste est vide")
 
    elif chiffre == 3:
       print("Adieu")
       break
    else:
        print("Taper l'un des numéros demandé")
        continue