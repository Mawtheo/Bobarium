/**
 * BTS-CIEL2 :: CLIENT
 */

import React, { useState, useEffect } from 'react';
import { Text, View, Button, TextInput, StyleSheet } from "react-native";

// Adresse et port du serveur EV3
const PORT = 1664;

export default function Index() {
  const [commandeText, setcommandeText] = useState("Réception des commandes");
  const [sensorText, setSensorText] = useState("Données des capteurs");
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [adresseIP, setAdresseIP] = useState("");

  useEffect(() => {
    let interval;
    if (isRefreshing) {
      interval = setInterval(() => {
        sendCommand("capteurs");
      }, 1000);
    } else {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isRefreshing]);

  const sendCommand = async (command) => {
    try {
      const response = await fetch(`http://${adresseIP}:${PORT}/${command}`);
      console.log("Etat de la réponse:", response.status);

      if (response.ok) {
        const jsonResponse = await response.json();
        console.log("JSON:", jsonResponse);

        // Convertir la réponse JSON en une chaîne de caractères
        const responseString = JSON.stringify(jsonResponse, null, 2);

        if (command === "capteurs") {
          setSensorText(responseString);
        } else {
          setcommandeText(responseString);
        }
      }

    } catch (error) {
      console.error("Erreur lors de l'envoi de la commande:", error);
      if (command === "capteurs") {
        setSensorText("Erreur: " + error.message);
      } else {
        setcommandeText("Erreur: " + error.message);
      }
    }
  };

  const toggleRefreshing = () => {
    setIsRefreshing(!isRefreshing);
    if (!isRefreshing) {
      sendCommand("capteurs");
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.ipInputContainer}>
        <TextInput
          style={styles.ipInput}
          placeholder="Entrez l'adresse IP"
          value={adresseIP}
          onChangeText={setAdresseIP}
          keyboardType="numeric"
        />
      </View>
      <View style={styles.refreshButtonContainer}>
        <Button title={isRefreshing ? "Arrêter Capteurs" : "Capteurs"} onPress={toggleRefreshing} />
      </View>
      <Text style={styles.sensorText}>{sensorText}</Text>
      <View style={styles.commande}>
        <Button title="Barre_Up" onPress={() => sendCommand("barre_up")} />
        <Button title="Barre_Down" onPress={() => sendCommand("barre_down")} />
        <Button title="LED On" onPress={() => sendCommand("led_on")} />
        <Button title="LED Off" onPress={() => sendCommand("led_off")} />
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
      <View style={styles.stop}>
      <Button title="Stop" onPress={() => sendCommand("stop")} />
      </View>
      <Text style={styles.commandeText}>{commandeText}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#dfdcdc",
    alignItems: "center",
  },
  ipInputContainer: {
    marginTop: 20,
    marginBottom: 20,
    width: "80%",
  },
  ipInput: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
  refreshButtonContainer: {
    marginTop: 20,
    marginBottom: 20,
  },
  sensorText: {
    marginTop: 20,
    padding: 10,
    backgroundColor: "#fffebf",
    borderRadius: 5,
    borderWidth: 1,
    borderColor: "#ccc",
    width: "90%",
    textAlign: "center",
  },
  commande: {
    flex: 1,
    justifyContent: "center",
    alignItems: "stretch",
  },
  avancer: {
    bottom: 70
  },
  reculer: {
    bottom: -15
  },
  gauche: {
    bottom: 85,
    right: 105
  },
  droite: {
    bottom: 120,
    left: 100
  },
  stop: {
    bottom: 155,
    right: 0,
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