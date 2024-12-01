/**
 * BTS-CIEL2 :: CLIENT
 */

import React, { useState } from 'react';
import { Text, View, Button, StyleSheet } from "react-native";

// Adresse et port du serveur EV3
const ADRESSE = "10.0.0.6";
const PORT = 1664;

export default function Index() {

  const [commandeText, setcommandeText] = useState("Réception des commandes");

  const sendCommand = async (command) => {
    try {
      const response = await fetch(`http://${ADRESSE}:${PORT}/${command}`);
      console.log("Etat de la réponse:", response.status);

      if (response.ok) {
        const jsonResponse = await response.json();
        console.log("JSON:", jsonResponse);
        setcommandeText(JSON.stringify(jsonResponse, null, 2));
      }

    } catch (error) {
      console.error("Erreur lors de l'envoi de la commande:", error);
      setcommandeText("Erreur: " + error.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text>Théo et Valérian vous présente Bobarium !</Text>
      <View style={styles.commande}>
        <Button title="Stop" onPress={() => sendCommand("stop")} />
        <Button title="Barre"onPress={() => sendCommand("barre")} />
        <Button title="Distance" onPress={() => sendCommand("distance")} />
        <Button title="LED On" onPress={() => sendCommand("led_on")} />
        <Button title="LED Off" onPress={() => sendCommand("led_off")} />
        <Button title="Bobarium" onPress={() => sendCommand("bobarium")} />
        <Button title="Gyro" onPress={() => sendCommand("angle_robot")} />
        <Button title="Angle roues" onPress={() => sendCommand("angle_roue")} />
      </View>
      <View style={styles.avancer}>
        <Button title="Avancer" color="#ff8700" onPress={() => sendCommand("avancer")} />
      </View>
      <View style={styles.reculer}>
        <Button title="Reculer" color="#ff8700" onPress={() => sendCommand("reculer")} />
      </View>
      <View style={styles.gauche}>
        <Button title="Gauche" color="#ff8700" onPress={() => sendCommand("gauche")} />
      </View>
      <View style={styles.droite}>
        <Button title="Droite" color="#ff8700" onPress={() => sendCommand("droite")} />
      </View>
      <Text style={styles.commandeText}>{commandeText}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#d7ded9",
    alignItems: "center",
  },
  commande: {
    flex: 1,
    justifyContent: "center",
    alignItems: "stretch",
  },
  avancer: {
    bottom: 60
  },
  reculer: {
    bottom: 0
  },
  gauche: {
    bottom: 85,
    right: 105
  },
  droite: {
    bottom: 120,
    left: 100
  },
  commandeText: {
    marginTop: 20,
    padding: 10,
    backgroundColor: "#fff",
    borderRadius: 5,
    borderWidth: 1,
    borderColor: "#ccc",
    width: "90%",
    textAlign: "center",
  },
});
