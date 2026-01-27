import machine
import utime

temp_sensor = machine.ADC(4)

while True:
    reading = temp_sensor.read_u16()
    voltage = reading * 3.3 / 65535
    temperature = 27 - (voltage - 0.706) / 0.001721

    print("Temperature:", temperature, "°C")
    utime.sleep(1)
