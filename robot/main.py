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
# Création des moteurs
left_m = Motor(Port.A, Direction.CLOCKWISE)
right_m = Motor(Port.C, Direction.CLOCKWISE)
medium_m = Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(left_m, right_m, wheel_diameter=55.5, axle_track=104)

# Son de boot
ev3.speaker.play_file(SoundFile.READY)

# Fonctions des ordres 
def avancer():
    robot.straight(1000)

def reculer():
    robot.straight(-1000)

def stop():
    robot.stop()
    
def gauche():
    robot.turn(-10)

def droite():
    robot.turn(10)

def barre():
    medium_m.run(-1000)
    wait(1000)
    medium_m.stop()
    medium_m.run(+1000)
    wait(1000)
    medium_m.stop()

def distance():
    ultrasonic = UltrasonicSensor(Port.S2)
    distance = ultrasonic.distance(silent=True)
    print("distance = ", distance, "mm")

def led_on():
    ev3.light.on(Color.RED)

def led_off():
    ev3.light.off()

def bobarium():
    capteur = ColorSensor(Port.S3)
    taux = capteur.reflection()
    if taux <= 10:
        print("bobarium détecté = ", taux)
    else:
        print("taux = ", taux)

def gyro():
    angle = GyroSensor(Port.S4)
    angle.speed()
    print("angle = ", angle)


# Adresse ip du robot
ADRESSE = "192.168.1.153"
PORT = 1664

def run():
    # Création d'une socket
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # On demande à l'OS d'attacher notre programme au port TCP demandé
    serveur.bind((ADRESSE, PORT))
    serveur.listen(10)

    while True:
        client, adresse = serveur.accept()
        print("Connexion établie avec", adresse)

        # Réception de la requete du client sous forme de bytes et transformation en string
        requete = client.recv(1024)
        print("requete reçue: ", requete.decode())

        # Traiter les requêtes GET
        if "GET" in requete.decode():
            # Extraire l'URL de la requête
            url_part = requete.decode().split(" ")[1]  # Extrait l'URL de la requête
            print("URL:", url_part)

            # Commandes du robot
            if "/avancer" in url_part:
                avancer()
            elif "/reculer" in url_part:
                reculer()
            elif "/gauche" in url_part:
                gauche()
            elif "/droite" in url_part:
                droite()
            elif "/stop" in url_part:
                stop()
            elif "/barre" in url_part:
                barre()
            elif "/distance" in url_part:
                distance()
            elif "/led_on" in url_part:
                led_on()
            elif "/led_off" in url_part:
                led_off()
            elif "/bobarium" in url_part:
                bobarium()
            elif "/gyro" in url_part:
                gyro()
            else:
                print("Commande non reconnue dans l'URL")

        # Envoi d'une réponse HTTP (réponse simple en texte HTML)
        reponse = "HTTP/1.1 200 OK\r\n"
        reponse += "Server: Sioux/1.3.3.7\r\n"
        reponse += "Content-Type: text/html\r\n"
        reponse += "Content-Length: 14\r\n"
        reponse += "\r\n"
        reponse += "<h1>Commande envoyer</h1>"

        client.send(reponse.encode())

        # Déconnexion avec le client
        print("Fermeture de la connexion avec le client.")
        client.close()

if __name__ == "__main__":
    run()