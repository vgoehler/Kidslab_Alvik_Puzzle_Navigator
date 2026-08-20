from arduino_alvik import ArduinoAlvik
from time import sleep_ms, ticks_ms


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
    """Blink the left and right LEDs of the Arduino Alvik alternately."""
    end_time = ticks_ms() + duration

    while True:
        # Left LED on, right LED off
        alvik.left_led.set_color(1, 0, 0)   # red
        alvik.right_led.set_color(0, 0, 0)  # off
        sleep_ms(interval)

        # Right LED on, left LED off
        alvik.left_led.set_color(0, 0, 0)   # off
        alvik.right_led.set_color(0, 0, 1)  # blue
        sleep_ms(interval)

        if ticks_ms() >= end_time:
            break

    # Turn both LEDs off
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)


def run_color_react(alvik):
    DISTANCE_THRESHOLD = 5  # cm
    CENTER_TOF = 2  # 5 indices (left, centerleft, center, centerright, right)

    while True:
        # Stop if cancel button pressed
        if alvik.get_touch_cancel():
            stop_robot(alvik)
            print("Cancelled by user.")
            break

        # Check distance sensor
        rel_dist = alvik.get_distance_bottom()
        if rel_dist < DISTANCE_THRESHOLD:
            stop_robot(alvik)
            print(f"Obstacle detected: {rel_dist} cm")
            blink_alternating_leds(alvik, duration=5000)
            break

        # Check color sensor and act accordingly
        color = alvik.get_color_label()
        if color == "GREEN" or color == "LIGHT GREEN":
            print("Green detected: turn right 90° and move 3 cm.")
            stop_robot(alvik)
            turn_right(alvik)
            move_3cm(alvik)
        elif color == "RED":
            print("Red detected: turn left 90° and move 3 cm.")
            stop_robot(alvik)
            turn_left(alvik)
            move_3cm(alvik)
        elif color == "BLUE" or color == "LIGHT BLUE":
            print("Blue detected: turn 180° and move 3 cm.")
            stop_robot(alvik)
            turn_180(alvik)
            move_3cm(alvik)
        else:
            print(f"Color: {color} detected. Moving forward.")
            move_forward(alvik)

        # Short pause for sensor stability
        sleep_ms(100)


if __name__ == "__main__":
    alvik = ArduinoAlvik()
    alvik.begin()
    run_color_react(alvik)