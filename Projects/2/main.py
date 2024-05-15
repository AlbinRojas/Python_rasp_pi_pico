from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

while True:
    if button.value() == 0:
        led.toggle()
        print("hello")
        time.sleep(0.5)
