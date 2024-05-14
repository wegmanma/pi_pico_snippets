from machine import Pin
from neopixel import NeoPixel

        
gpio = 21
led_pin = Pin(gpio,Pin.OUT)
led_count = 4
np = NeoPixel(led_pin,led_count)


for i in range(4):
    np[i] = [193+25,131-92,251-131]
np.write()
        
