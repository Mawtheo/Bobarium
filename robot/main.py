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
    print("distance", distance, "mm")

def led_on():
    ev3.light.on(Color.RED)

def led_off():
    ev3.light.off()

def bobarium():
    lazer=ColorSensor(Port.S3)
    taux = lazer.reflection()
    if taux <= 10:
        print("bobarium détecté", taux)
    else:
        print(taux)



# Adresse ip du robot
ADRESSE = "192.168.1.153"
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
            avancer()
        if requete.decode() == "reculer":
            reculer()
        if requete.decode() == "gauche":
            gauche()
        if requete.decode() == "droite":
            droite()
        if requete.decode() == "stop":
            stop()
        if requete.decode() == "barre":
            barre()
        if requete.decode() == "distance":
            distance()
        if requete.decode() == "led_on":
            led_on()
        if requete.decode() == "led_off":
            led_off()
        if requete.decode() == "bobarium":
            bobarium()

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