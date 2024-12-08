#
# <p align="center">Bobarium</p>
  

## 🛠️ Guide d'installation

### Sur Windows

- Installer NodeJS  
[NodeJS](https://nodejs.org/en/)
- Installer les packages pour NodeJS  
`npm install`
- Lancer l'application dans le dossier  
`/Bobarium/ihm/`  
avec `npx expo start`

### Sur le robot

![LegoBrick](https://imgs.search.brave.com/c5Q_41gKd0YcbN3Rmht6MYbvIVL0PmQKN2ihwIswW3Q/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/YnJpY2tvd2wuY29t/L2ZpbGVzL2ltYWdl/X2NhY2hlL2xhcmdl/L2xlZ28tZXYzLWlu/dGVsbGlnZW50LWJy/aWNrLXNldC00NTUw/MC0xMTc5NzUuanBn)

- Installer VSCode  
[VSCode](https://code.visualstudio.com/)
- Télécharger l'extension  
`LEGO® MINDSTORMS® EV3 MicroPython`
- Connecter votre robot lego avec l'addresse ip indiqué
- Téléverser le fichier sur le robot  
`/Bobarium/robot/main.py`

### Sur le smartphone

- Installer Expo Go  
[ExpoGo](https://expo.dev/go)

## ➤ API


```http
GET ADRESSE_IP/PORT/COMMAND
```
| Command |  Return | Description |
| :-------- | :------- | :------------------------- |
| `stop`   | `'stop'` | **Stop le robot**|
| `barre_up`  | `'barre_up'` | **Lève barre**|
| `barre_down`  | `'barre_down'` | **Descend barre**|
| `led_on`| `'led_on'` | **Allume led en rouge**|
| `led_off`| `'led_off'` | **Eteind led**|
| `capteurs`| `$distance, $bobarium, $angle_robot, $angle_roue` | **Réception des valeurs des capteurs**|
| `avancer`| `'avancer'` | **Robot avance**|
| `reculer`| `'reculer'` | **Robot recule**|
| `gauche`| `'gauche'` | **Robot va à gauche**|
| `droite`| `'droite` | **Robot va à droite**|

## 🗒️ Répartissement des tâches

- Voir le kanban  
[Kanban](https://github.com/users/Mawtheo/projects/1)