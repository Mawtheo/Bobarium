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
import json

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
    left_m.run(250)
    right_m.run(250)

def reculer():
    left_m.run(-250)
    right_m.run(-250)
    
def gauche():
    left_m.run_time(speed=-250, time=800, wait=False)
    right_m.run_time(speed=250, time=800, wait=False)

def droite():
    left_m.run_time(speed=250, time=800, wait=False)
    right_m.run_time(speed=-250, time=800, wait=False)

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
    return distance

# Taux de bobarium
def bobarium():
    taux = colorsensor.reflection()
    return taux

# Position angulaire du robot en degrès
def angle_robot():
    angle = gyrosensor.angle()
    return angle

def angle_roue():
    angle_droit = right_m.angle()
    angle_gauche = left_m.angle()
    return angle_droit, angle_gauche

# chifrement XOR
def chifrement(data, key):
    result = bytearray()
    for i in range(len(data)):
        result.append(data[i] ^ key[i % len (key)])
    return bytes(result)

# Adresse IP du robot
ADRESSE = "192.168.1.116"
PORT = 1664

def run():
    # Création d'une socket
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # On demande à l'OS d'attacher notre programme au port TCP demandé
    serveur.bind((ADRESSE, PORT))
    serveur.listen(1)

    while True:
        client, adresse = serveur.accept()
        print("Connexion établie avec", adresse)

        while True:
            # Réception de la requete du client sous forme de bytes et transformation en string
            requete = client.recv(2048)
            print("requete reçue: ", requete.decode())

            # Réponse JSON à envoyer en HTTP
            json_reponse = {}

            # Traiter requêtes GET
            if "GET" in requete.decode():
                # Extraire l'URL de la requête
                url_part = requete.decode().split(" ")[1]
                print("ENDPOINT:", url_part)

                # Commandes du robot
                if "/avancer" in url_part:
                    avancer()
                    json_reponse = {"commande": "avancer"}
                elif "/reculer" in url_part:
                    reculer()
                    json_reponse = {"commande": "reculer"}
                elif "/gauche" in url_part:
                    gauche()
                    json_reponse = {"commande": "gauche"}
                elif "/droite" in url_part:
                    droite()
                    json_reponse = {"commande": "droite"}
                elif "/stop" in url_part:
                    stop()
                    json_reponse = {"commande": "stop"}
                elif "/barre" in url_part:
                    barre()
                    json_reponse = {"commande": "barre"}
                elif "/led_on" in url_part:
                    led_on()
                    json_reponse = {"commande": "led_on"}
                elif "/led_off" in url_part:
                    led_off()
                    json_reponse = {"commande": "led_off"}
                elif "/capteurs" in url_part:
                    data1 = distance()
                    data2 = bobarium()
                    data3 = angle_robot()
                    data4 = angle_roue()
                    json_reponse = {"commande": "capteurs", "distance": data1, "bobarium": data2, "angle_robot": data3, "angle_roue_droit": data4[0], "angle_roue_gauche": data4[1]}
                else:
                    print("Mauvais endpoint ;)")
                    json_reponse = {"commande": "erreur"}

            # Envoi d'une réponse HTTP (réponse en JSON)
            reponse = "HTTP/1.1 200 OK\r\n"
            reponse += "Server: Sioux/1.3.3.7\r\n"
            reponse += "Content-Type: application/json\r\n"
            reponse += "Content-Length: {}\r\n".format(len(json.dumps(json_reponse)))
            reponse += "\r\n"
            reponse += json.dumps(json_reponse)


            client.send(reponse.encode())

        # Déconnexion avec le client
        print("Fermeture de la connexion avec le client.")
        client.close()

        # Arrêt du serveur
        print("Arrêt du serveur.")
        serveur.close()

if __name__ == "__main__":
    run()