"""
BTS-CIEL2 :: SERVEUR
"""

# Libraries
import socket
import json

# Simulated robot commands
def avancer():
    print("Robot is moving forward.")

def reculer():
    print("Robot is moving backward.")

def gauche():
    print("Robot is turning left.")

def droite():
    print("Robot is turning right.")

def stop():
    print("Robot has stopped.")

def barre():
    print("Bar is moving up and down.")

def led_on():
    print("LED is on.")

def led_off():
    print("LED is off.")

def distance():
    simulated_distance = 500  # Simulated distance in mm
    print("Distance =", simulated_distance, "mm")
    return simulated_distance

def bobarium():
    simulated_taux = 5  # Simulated bobarium level
    print("Bobarium detected =", simulated_taux, "%")
    return simulated_taux

def angle_robot():
    simulated_angle = 90  # Simulated robot angle in degrees
    print("Robot angle =", simulated_angle, "°")
    return simulated_angle

def angle_roue():
    simulated_angle_droit = 45  # Simulated right wheel angle in degrees
    simulated_angle_gauche = 45  # Simulated left wheel angle in degrees
    print("Right wheel angle =", simulated_angle_droit, "°")
    print("Left wheel angle =", simulated_angle_gauche, "°")
    return simulated_angle_droit, simulated_angle_gauche

# XOR cryptage
def chifrement(data, key):
    result = bytearray()
    for i in range(len(data)):
        result.append(data[i] ^ key[i % len(key)])
    return bytes(result)

# Server address and port
ADRESSE = "10.0.0.6"
PORT = 1664

def run():
    # Create a socket
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    serveur.bind((ADRESSE, PORT))
    serveur.listen(1)

    # Clé de chiffrement
    KEY = b"&%Tv@SmMDR2597cL"

    while True:
        client, adresse = serveur.accept()
        print("Connection established with", adresse)

        while True:
            # Receive the request from the client
            requete = client.recv(2048)
            print("Request received:", requete.decode())
            
            # JSON response to send in HTTP
            json_reponse = {}

            # Handle GET requests
            if "GET" in requete.decode():
                # Extract the URL part of the request
                url_part = requete.decode().split(" ")[1]
                print("URL:", url_part)

                # Robot commands
                if "/avancer" in url_part:
                    avancer()
                    json_reponse = {"commande": str(chifrement(KEY, b"avancer"))}
                elif "/reculer" in url_part:
                    reculer()
                    json_reponse = {"commande": str(chifrement(KEY, b"reculer"))}
                elif "/gauche" in url_part:
                    gauche()
                    json_reponse = {"commande": str(chifrement(KEY, b"gauche"))}
                elif "/droite" in url_part:
                    droite()
                    json_reponse = {"commande": str(chifrement(KEY, b"droite"))}
                elif "/stop" in url_part:
                    stop()
                    json_reponse = {"commande": str(chifrement(KEY, b"stop"))}
                elif "/barre" in url_part:
                    barre()
                    json_reponse = {"commande": str(chifrement(KEY, b"barre"))}
                elif "/led_on" in url_part:
                    led_on()
                    json_reponse = {"commande": str(chifrement(KEY, b"led_on"))}
                elif "/led_off" in url_part:
                    led_off()
                    json_reponse = {"commande": str(chifrement(KEY, b"led_off"))}
                elif "/distance" in url_part:
                    data = distance()
                    json_reponse = {"commande": str(chifrement(KEY, b"distance")), "data": str(chifrement(KEY, bytes(data)))}
                elif "/bobarium" in url_part:
                    data = bobarium()
                    json_reponse = {"commande": str(chifrement(KEY, b"bobarium")), "data": str(chifrement(KEY, bytes(data)))}
                elif "/angle_robot" in url_part:
                    data = angle_robot()
                    json_reponse = {"commande": str(chifrement(KEY, b"angle_robot")), "data": str(chifrement(KEY, bytes(data)))}
                elif "/angle_roue" in url_part:
                    data = angle_roue()
                    json_reponse = {"commande": str(chifrement(KEY, b"angle_roue")), "data": str(chifrement(KEY, bytes(data)))}
                else:
                    print("Invalid endpoint ;)")
                    json_reponse = {"commande": str(chifrement(KEY, b"erreur"))}

            # Send an HTTP response (JSON response)
            reponse = "HTTP/1.1 200 OK\r\n"
            reponse += "Server: Sioux/1.3.3.7\r\n"
            reponse += "Content-Type: application/json\r\n"
            reponse += "Content-Length: {}\r\n".format(len(json.dumps(json_reponse)))
            reponse += "\r\n"
            reponse += json.dumps(json_reponse)

            client.send(reponse.encode())

        # Close the connection with the client
        print("Closing connection with the client.")
        client.close()

        # Stop the server
        print("Stopping the server.")
        serveur.close()

if __name__ == "__main__":
    run()
