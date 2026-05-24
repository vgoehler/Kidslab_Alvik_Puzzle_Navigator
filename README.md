# Kidslab Alvik Puzzle Navigator

Dieses Repository enthält den Code und die 3D-Druckdateien für eine der Stationen, die wir im **Kidslab an der TU Bergakademie Freiberg** am **09.05.2026** durchgeführt haben.

🔗 [Event-Ankündigung: Freiberger Alumni Netzwerk](https://freiberger-alumni-netzwerk.de/events/211/)

---

## Über das Projekt

An der Station haben Kinder mit dem **Arduino Alvik** – einem kleinen Roboter, der in MicroPython programmiert wird – experimentiert.
Es standen **4 Roboter** bereit, damit viele Kinder gleichzeitig teilnehmen konnten.

Die Kinder konnten die **Umgebung verändern** (z. B. farbige Felder auf der Fahrbahn umstellen oder Hindernisse platzieren), um das **Verhalten des Roboters zu beobachten und zu verstehen**.

---

## Modi

Der Roboter startet ein einfaches Menü. Mit den **Up/Down-Tasten** wird der Modus gewählt, mit **OK** gestartet und mit **Cancel** gestoppt.

### 0 · Linienverfolger (`line_follower.py`)

> Basiert auf der offiziellen **Arduino Alvik Demo**.

Der Roboter folgt einer schwarzen Linie mithilfe der drei Liniensensoren (links, mitte, rechts). Ein P-Regler berechnet den Fehler und steuert die Radgeschwindigkeit entsprechend. Die LEDs zeigen an, ob der Roboter die Linie hält (grün) oder korrigiert (rot).

### 1 · Farbreaktion (`simple_drive_and_color_react.py`)

Der Roboter fährt geradeaus und reagiert auf farbige Felder:

| Farbe | Aktion |
|-------|--------|
| 🟩 Grün / Hellgrün | 90° rechts drehen, 3 cm fahren |
| 🟥 Rot | 90° links drehen, 3 cm fahren |
| 🟦 Blau / Hellblau | 180° drehen, 3 cm fahren |
| Alles andere | Geradeaus weiterfahren |

Bei einem Hindernis näher als 5 cm stoppt der Roboter und die LEDs blinken abwechselnd.

---

## Projektstruktur

```
├── Code/
│   ├── main.py                        # Einstiegspunkt: Menü zum Auswählen der Modi
│   ├── choices.py                     # Imports für das Menü
│   ├── line_follower.py               # Modus 0: Linienverfolger (aus der Alvik-Demo)
│   └── simple_drive_and_color_react.py  # Modus 1: Farbbasiertes Navigieren
└── 3d-Files/
    ├── Fusion360/                     # Bearbeitbare Quelldateien (Fusion 360 / IGES)
    └── Mesh/                          # Druckfertige Dateien (.3mf)
```

### 3D-Druckteile

Die gedruckten Teile bilden eine modulare Fahrstrecke aus Platten und Ecken:

| Datei | Beschreibung |
|-------|-------------|
| `Kidslab Platte` | Standard-Fahrbahnplatte |
| `Kidslab Platte Start` | Startplatte |
| `Kidslab Platte End` | Zielplatte |
| `Kidslab Platte - Outside Marker` | Platte mit äußerer Markierung |
| `Kidslab Ecke Vorn Links/Rechts` | Kurve vorne links / rechts |
| `Kidslab Ecke Hinten Links/Rechts` | Kurve hinten links / rechts |

---

## Hardware

- [Arduino Alvik](https://store.arduino.cc/products/arduino-alvik) (×4)
- MicroPython-Firmware

---

## Lizenz

Siehe [LICENSE](LICENSE).
