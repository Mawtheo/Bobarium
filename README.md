#
# <p align="center">Bobarium</p>
  

## 🛠️ Guide d'utilisation
- Sur windows activer les droits via CMD  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Installer les packages  pour Node JS  
`npm install`
- Lancer l'application  
`npx expo start`


![LegoBrick](https://imgs.search.brave.com/c5Q_41gKd0YcbN3Rmht6MYbvIVL0PmQKN2ihwIswW3Q/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/YnJpY2tvd2wuY29t/L2ZpbGVzL2ltYWdl/X2NhY2hlL2xhcmdl/L2xlZ28tZXYzLWlu/dGVsbGlnZW50LWJy/aWNrLXNldC00NTUw/MC0xMTc5NzUuanBn)
        

## ➤ API


```http
GET ADRESSE_IP/PORT/COMMAND
```
| Command |  Return | Description            |
| :-------- | :------- | :------------------------- |
| `stop`   | `'stop'` | **Stop le robot**|
| `barre`  | `'barre'` | **Lève / descend barre**|
| `led_on`| `'led_on'` | **Allume led en rouge**|
| `led_off`| `'led_off'` | **Eteind led**|
| `capteurs`| `$distance, $bobarium, $angle_robot, $angle_roue` | **Réception des valeurs des capteurs**|
| `avancer`| `'avancer'` | **Robot avance**|
| `reculer`| `'reculer'` | **Robot recule**|
| `gauche`| `'gauche'` | **Robot va à gauche**|
| `droite`| `'droite` | **Robot va à droite**|