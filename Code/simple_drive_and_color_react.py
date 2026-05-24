from arduino_alvik import ArduinoAlvik
from time import sleep_ms, ticks_ms

if __name__ == "__main__":
  alvik = ArduinoAlvik()
  alvik.begin()
  run_color_react(alvik)

def stop_robot(alvik):
    alvik.brake()

def move_forward(alvik):
    alvik.drive(linear_velocity=25, angular_velocity=0, linear_unit='cm/s')

def turn_right(alvik):
    alvik.rotate(angle=90, unit='deg', blocking=True)

def turn_left(alvik):
    alvik.rotate(angle=-90, unit='deg', blocking=True)

def turn_180(alvik):
    alvik.rotate(angle=180, unit='deg', blocking=True)

def move_3cm(alvik):
    alvik.move(distance=3, unit='cm', blocking=True)


def blink_alternating_leds(alvik, interval=500, duration=1000):
    """
    Lässt die linke und rechte LED des Arduino Alvik abwechselnd blinken.
    """
    end_time = ticks_ms() + duration

    while True:
        # Linke LED an, rechte LED aus
        alvik.left_led.set_color(1, 0, 0)  # Rot
        alvik.right_led.set_color(0, 0, 0)  # Aus
        sleep_ms(interval)

        # Rechte LED an, linke LED aus
        alvik.left_led.set_color(0, 0, 0)  # Aus
        alvik.right_led.set_color(0, 0, 1)  # Blau
        sleep_ms(interval)

        # Abbruch, wenn duration_sec abgelaufen ist
        if ticks_ms() >= end_time:
            break

    # Beide LEDs ausschalten
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)

def run_color_react(alvik):
    # Konstanten
    DISTANCE_THRESHOLD = 5  # cm
    GRID_SIZE = 5  # cm
    CENTER_TOF = 2 # 5 indices (left, centerleft, center, centerright, right)
 
    while True:
        # Abbruch durch X-Taste (Cancel) oder Hindernis
        if alvik.get_touch_cancel():
            stop_robot(alvik)
            print("Abbruch durch X-Taste.")
            break

        # Distanzsensor prüfen (center_tof)
        #distances = alvik.get_distance(unit='cm')
        #rel_dist = distances[CENTER_TOF]
        rel_dist = alvik.get_distance_bottom()
        if rel_dist < DISTANCE_THRESHOLD:
            stop_robot(alvik)
            print(f"Hindernis erkannt: {rel_dist} cm")
            blink_alternating_leds(alvik, duration=5000)
            break

        # Farbsensor prüfen
        color = alvik.get_color_label()
        if color == "GREEN" or color == "LIGHT GREEN":
            print("Grün erkannt: 90° rechts drehen und 3 cm fahren.")
            stop_robot(alvik)
            turn_right(alvik)
            move_3cm(alvik)
        elif color == "RED":
            print("Rot erkannt: 90° links drehen und 3 cm fahren.")
            stop_robot(alvik)
            turn_left(alvik)
            move_3cm(alvik)
        elif color == "BLUE" or color == "LIGHT BLUE":
            print("Blau erkannt: 180° drehen und 3 cm fahren.")
            stop_robot(alvik)
            turn_180(alvik)
            move_3cm(alvik)
        else:
            # Standard: Geradeaus fahren
            print(f"Farbe: {color} erkannt. no action.")
            move_forward(alvik)

        # Kurze Pause für Sensorstabilität
        sleep_ms(100)