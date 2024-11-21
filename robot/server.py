import socket

ADRESSE = "192.168.1.156"
PORT = 1664

def run():
    # Création d'une socket
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # On demande à l'OS d'attacher notre programme au port TCP demandé
    serveur.bind((ADRESSE, PORT))
    serveur.listen(10)

    client, adresse = serveur.accept()
    fin = False
    while fin == False:
        # Réception de la requete du client sous forme de bytes et transformation en string
        requete = client.recv(1024)
        print("requete reçue: ", requete.decode())
        if requete.decode() == "FIN":
            fin = True
        
        # Commandes du robot
        if requete.decode() == "avancer":
            print("Avancer")
        if requete.decode() == "reculer":
            print("Reculer")
        if requete.decode() == "gauche":
            print("Gauche")
        if requete.decode() == "droite":
            print("Droite")
        if requete.decode() == "stop":
            print("Stop")
        if requete.decode() == "barre":
            print("Barre")
        if requete.decode() == "distance":
            print("Distance")
        if requete.decode() == "led_on":
            print("Led_on")
        if requete.decode() == "led_off":
            print("Led_off")

        # Préparation et envoi de la réponse
        reponse = "OK"
        client.send(reponse.encode())

    # Déconnexion avec le client
    print("Fermeture de la connexion avec le client.")
    client.close()

    # Arrêt du serveur    
    print("Arret du serveur.")
    serveur.close()
    

if __name__ ==  "__main__":
    run()