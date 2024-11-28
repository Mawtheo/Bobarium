/**
 * BTS-CIEL2 :: CLIENT
 */

import { Text, View, Button, StyleSheet} from "react-native";

// Adresse et port du serveur EV3
const ADRESSE = "192.168.1.170";
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
      <Text>Théo et Valérian vous présente Bobarium !</Text>

      <View style={styles.commande}>
        <Button title="Stop" color="#4d6bff" onPress={() => sendCommand("stop")} />
        <Button title="Barre" color="#4d6bff" onPress={() => sendCommand("barre")} />
        <Button title="Distance" color="#4d6bff" onPress={() => sendCommand("distance")} />
        <Button title="LED On" color="#4d6bff" onPress={() => sendCommand("led_on")} />
        <Button title="LED Off" color="#4d6bff" onPress={() => sendCommand("led_off")} />
        <Button title="Bobarium" color="#4d6bff" onPress={() => sendCommand("bobarium")} />
        <Button title="Gyro" color="#4d6bff" onPress={() => sendCommand("gyro")} />
        <Button title="Angle roues" color="#4d6bff" onPress={() => sendCommand("angle_roue")} />
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
  }
})