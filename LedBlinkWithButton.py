from machine import Pin
import utime

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
     led.value(1)
     utime.sleep(1)
     led.value(0)
    
