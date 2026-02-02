from machine import Pin, I2C
import ssd1306
import time

# I2C setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# OLED setup (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_face():
    oled.fill(0)

    # Face outline (circle-ish)
    oled.ellipse(64, 32, 28, 28, 1)

    # Eyes 🙂
    oled.fill_rect(50, 24, 6, 6, 1)   # Left eye
    oled.fill_rect(72, 24, 6, 6, 1)   # Right eye

    # Smile
    oled.arc(64, 38, 14, 8, 20, 160, 1)

    oled.show()

while True:
    draw_face()
    time.sleep(2)