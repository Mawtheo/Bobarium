#!/usr/bin/env pybricks-micropython

"""
BTS-CIEL2 :: SERVEUR
"""

# Librairies
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import socket

# Initialisation des commandes du robot
ev3 = EV3Brick()

# Initialisation des moteurs
left_m = Motor(Port.A, Direction.CLOCKWISE)
right_m = Motor(Port.C, Direction.CLOCKWISE)
medium_m = Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(left_m, right_m, wheel_diameter=55.5, axle_track=104)

# Initialisation des capteurs
ultrasonic = UltrasonicSensor(Port.S2)
colorsensor = ColorSensor(Port.S3)
gyrosensor = GyroSensor(Port.S4)

# Son de boot
ev3.speaker.play_file(SoundFile.READY)

# Fonctions des ordres 
def avancer():
    left_m.run(500)
    right_m.run(500)

def reculer():
    left_m.run(-500)
    right_m.run(-500)
    
def gauche():
    left_m.run_time(speed=-150, time=1000, wait=False)
    right_m.run_time(speed=150, time=1000, wait=False)

def droite():
    left_m.run_time(speed=150, time=1000, wait=False)
    right_m.run_time(speed=-150, time=1000, wait=False)

def stop():
    robot.stop()

# Lever / Baisser la barre
def barre():
    medium_m.run(-1000)
    wait(1000)
    medium_m.stop()
    medium_m.run(1000)
    wait(1000)
    medium_m.stop()

def led_on():
    ev3.light.on(Color.RED)

def led_off():
    ev3.light.off()

# Capteur ultrason permet de détecter les obstacles 
def distance():
    distance = ultrasonic.distance(silent=False)
    print("distance = ", distance, "mm")

# Taux de bobarium
def bobarium():
    taux = colorsensor.reflection()
    if taux <= 10:
        print("bobarium détecté = ", taux, "%")
    else:
        print("taux = ", taux, "%")

# Position angulaire du robot en degrès
def angle_robot():
    angle = gyrosensor.angle()
    print("angle robot = ", angle, "°")

def angle_roue():
    angle_droit = right_m.angle()
    angle_gauche = left_m.angle()
    print("angle roue droite = ", angle_droit, "°")
    print("angle roue gauche = ", angle_gauche, "°")

# chifrement XOR
def chifrement(data, key):
    result = bytearray()
    for i in range(len(data)):
        result.append(data[i] ^ key[i % len (key)])
    return bytes(result)

# Exemple d'utilisation
data = b"Ceci est un test de chiffrement XOR"
key = b"secret_key"
encrypted_data = chifrement(data, key)
print(encrypted_data)  # Affichera la sortie chiffrée
decrypted_data = chifrement(encrypted_data, key)
print(decrypted_data)

# Adresse IP du robot
ADRESSE = "192.168.1.173"
PORT = 1664

def run():
    # Création d'une socket
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # On demande à l'OS d'attacher notre programme au port TCP demandé
    serveur.bind((ADRESSE, PORT))
    serveur.listen(10)

    client, adresse = serveur.accept()
    print("Connexion établie avec", adresse)

    while True:

        # Réception de la requete du client sous forme de bytes et transformation en string
        requete = client.recv(1024)
        print("requete reçue: ", requete.decode())

        # Réponse à envoyer en HTTP
        REPONSE_COMMANDE = ""

        # Traiter requêtes GET
        if "GET" in requete.decode():
            # Extraire l'URL de la requête
            url_part = requete.decode().split(" ")[1]
            print("URL:", url_part)

            # Commandes du robot
            if "/avancer" in url_part:
                avancer()
                REPONSE_COMMANDE = "<h1>commande = avancer()</h1>"
            elif "/reculer" in url_part:
                reculer()
                REPONSE_COMMANDE = "<h1>commande = reculer()</h1>"
            elif "/gauche" in url_part:
                gauche()
                REPONSE_COMMANDE = "<h1>commande = gauche()</h1>"
            elif "/droite" in url_part:
                droite()
                REPONSE_COMMANDE = "<h1>commande = droite()</h1>"
            elif "/stop" in url_part:
                stop()
                REPONSE_COMMANDE = "<h1>commande = stop()</h1>"
            elif "/barre" in url_part:
                barre()
                REPONSE_COMMANDE = "<h1>commande = barre()</h1>"
            elif "/led_on" in url_part:
                led_on()
                REPONSE_COMMANDE = "<h1>commande = led_on()</h1>"
            elif "/led_off" in url_part:
                led_off()
                REPONSE_COMMANDE = "<h1>commande = led_off()</h1>"
            elif "/distance" in url_part:
                distance()
                REPONSE_COMMANDE = "<h1>commande = distance()</h1>"
            elif "/bobarium" in url_part:
                bobarium()
                REPONSE_COMMANDE = "<h1>commande = bobarium()</h1>"
            elif "/angle_robot" in url_part:
                angle_robot()
                REPONSE_COMMANDE = "<h1>commande = angle_robot()</h1>"
            elif "/angle_roue" in url_part:
                angle_roue()
                REPONSE_COMMANDE = "<h1>commande = angle_roue()</h1>"
            else:
                print("Mauvais endpoint ;)")
                REPONSE_COMMANDE = "<h1>ERREUR D'ENDPOINT !</h1>"

        # Envoi d'une réponse HTTP (réponse simple en texte HTML)
        reponse = "HTTP/1.1 200 OK\r\n"
        reponse += "Server: Sioux/1.3.3.7\r\n"
        reponse += "Content-Type: text/html\r\n"
        reponse += "Content-Length: {}\r\n".format(len(REPONSE_COMMANDE))
        reponse += "\r\n"
        reponse += REPONSE_COMMANDE

        client.send(reponse.encode())

        # Déconnexion avec le client
        print("Fermeture de la connexion avec le client.")
        client.close()

if __name__ == "__main__":
    run()