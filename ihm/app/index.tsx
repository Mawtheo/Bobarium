/**
 * BTS-CIEL2 :: CLIENT
 */

import { Text, View, Button, StyleSheet, Image } from "react-native";

// Adresse et port du serveur EV3
const ADRESSE = "192.168.1.153";
const PORT = 1664;

export default function Index() {
  const sendCommand = async (command: string) => {
    try {
      const response = await fetch(`http://${ADRESSE}:${PORT}/${command}`);
      if (response.ok) {
        console.log("Commande envoyée", "La commande a été envoyée avec succès.");
      } else {
        console.log("Erreur", "Impossible d'envoyer la commande.");
      }
    } catch (error) {
      console.error("Erreur lors de l'envoi de la commande:", error);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.mouvement}>
        <Text>Théo et Valérian vous présente Bobarium !</Text>
        <Button title="Avancer" color="red" onPress={() => sendCommand("avancer")} />
        <Button title="Reculer" color="red" onPress={() => sendCommand("reculer")} />
        <Button title="Gauche" color="red" onPress={() => sendCommand("gauche")} />
        <Button title="Droite" color="red" onPress={() => sendCommand("droite")} />
      </View>
      <View style={styles.commande}>
        <Button title="Stop" color="blue" onPress={() => sendCommand("stop")} />
        <Button title="Barre" color="blue" onPress={() => sendCommand("barre")} />
        <Button title="Distance" color="blue" onPress={() => sendCommand("distance")} />
        <Button title="LED On" color="blue" onPress={() => sendCommand("led_on")} />
        <Button title="LED Off" color="blue"onPress={() => sendCommand("led_off")} />
        <Button title="Bobarium" color="blue" onPress={() => sendCommand("bobarium")} />
        <Button title="Gyro" color="blue" onPress={() => sendCommand("gyro")} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  mouvement: {
    flex: 1,
    backgroundColor: 'black',
    justifyContent: "center",
    alignItems: "center",
  },
  commande: {
    flex: 2,
    backgroundColor: 'black',
    justifyContent: "center",
    alignItems: "center",
  }
});
