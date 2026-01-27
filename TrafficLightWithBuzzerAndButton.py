from machine import Pin
import utime
import _thread

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(12, Pin.OUT)

def traffic_lights():
    global pedestrian_allowed

while True:
    
    led1.value(4)
    led2.value(0)
    led3.value(0)
    utime.sleep(4)
    
    
    led1.value(0)
    led2.value(2)
    led3.value(0)
    utime.sleep(2)
    
    
    led1.value(0)
    led2.value(0)
    led3.value(5)
    utime.sleep(5)
    
def pedestrian_buzzer():
    while True:
        if pedestrian_allowed and button.value() == 1:
            buzzer.value(1)
        else:
            buzzer.value(0)
        utime.sleep(0.1)
    
_thread.start_new_thread(traffic_lights, ())

pedestrian_buzzer()

    