from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)
ledR = Pin(15, Pin.OUT)
ledG = Pin(11, Pin.OUT)
ledY = Pin(8, Pin.OUT)

while True:
    if button.value() == 0:
        ledR.value(1)
        ledG.value(1)
        ledY.value(1)
    else:
        ledR.value(0)
        ledG.value(0)
        ledY.value(0)
        time.sleep(0.1)