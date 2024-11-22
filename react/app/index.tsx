import { Text, View, Button, Alert } from "react-native";

// Adresse et port du serveur EV3
const ADRESSE = "192.168.1.153";
const PORT = 1664;

export default function Index() {
  const sendCommand = async (command:string) => {
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
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Théo et Valérian vous présente Bobarium !</Text>
      <Button title="Avancer" onPress={() => sendCommand("avancer")} />
      <Button title="Reculer" onPress={() => sendCommand("reculer")} />
      <Button title="Gauche" onPress={() => sendCommand("gauche")} />
      <Button title="Droite" onPress={() => sendCommand("droite")} />
      <Button title="Stop" onPress={() => sendCommand("stop")} />
      <Button title="Barre" onPress={() => sendCommand("barre")} />
      <Button title="Distance" onPress={() => sendCommand("distance")} />
      <Button title="LED On" onPress={() => sendCommand("led_on")} />
      <Button title="LED Off" onPress={() => sendCommand("led_off")} />
      <Button title="Bobarium" onPress={() => sendCommand("bobarium")} />
      <Button title="Gyro" onPress={() => sendCommand("gyro")} />
    </View>
  );
}
