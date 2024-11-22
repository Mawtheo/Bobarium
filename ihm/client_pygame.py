"""
BTS-CIEL2 :: CLIENT TCP
"""

# Librairies
import socket
import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption('BOBARIUM')

# Adresse ip du robot
HOST = "192.168.1.153"
PORT = 1664

# Création de la socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    # Connexion au serveur
    client.connect((HOST, PORT))
    print(f"Connexion vers {HOST}:{PORT} réussie.")
    break

fin = False
while fin is False:
    requete = ''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        # Envoi d'un message texte
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    requete = 'avancer'
                if event.key == pg.K_DOWN:
                    requete = 'reculer'
                if event.key == pg.K_LEFT:
                    requete = 'gauche'
                if event.key == pg.K_RIGHT:
                    requete = 'droite'
                if event.key == pg.K_SPACE:
                    requete = 'stop'
                if event.key == pg.K_BACKSPACE:
                    requete = 'barre'
                if event.key == pg.K_KP0:
                    requete = 'distance'
                if event.key == pg.K_KP1:
                    requete = 'led_on'
                if event.key == pg.K_KP2:
                    requete = 'led_off'
                if event.key == pg.K_KP3:
                    requete = 'bobarium'
                if event.key == pg.K_KP4:
                    requete = 'gyro'

    #Vérifie que le message n'est pas vide
    if requete != "":
        client.send(requete.encode())
        
        # Réception de la réponse du serveur
        reponse = client.recv(1024)
        print("Reception...")
        print(reponse.decode())

# Déconnexion
print("Deconnexion.")
client.close()
