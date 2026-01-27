import machine
import utime
import _thread

# Traffic light LEDs
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

# Button and buzzer
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

# Shared flag
button_pressed = False


# ---------------------------------
# Thread: Button reader
# ---------------------------------
def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)


# Start button thread
_thread.start_new_thread(button_reader_thread, ())


# ---------------------------------
# Main traffic light loop
# ---------------------------------
while True:

    # If pedestrian button pressed
    if button_pressed:
        led_red.value(1)

        # Buzzer beeps
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)

        button_pressed = False

    
    led_red.value(1)
    utime.sleep(5)

    led_amber.value(1)
    utime.sleep(2)

    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)

    # AMBER
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)

    led_amber.value(0)
