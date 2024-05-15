from machine import Pin
import time
import random

start_Button = Pin(14, Pin.IN, Pin.PULL_UP)
ledR = Pin(15, Pin.OUT)
ledG = Pin(11, Pin.OUT)
ledY = Pin(8, Pin.OUT)

state = "wait"

seq = [random.choice(["R", "G", "Y"])]


def Wait():
    global state
    
    ledR.value(1)
    ledG.value(1)
    ledY.value(1)
        
    if start_Button.value() == 0:
        state = "start"

def Start():
    global state
    
    ledR.value(0)
    ledG.value(0)
    ledY.value(0)
    
    time.sleep(1)
    state = "waves"

def Waves():
    global state, seq
    
    for i in seq:
        if i == "R":
            ledR.value(1)
            time.sleep(1)
            ledR.value(0)
            time.sleep(1)
            
        elif i == "G":
            ledG.value(1)
            time.sleep(1)
            ledG.value(0)
            time.sleep(1)
            
        elif i == "Y":
            ledY.value(1)
            time.sleep(1)
            ledY.value(0)
            time.sleep(1)
    
    new_color = random.choice(["R", "G", "Y"])
    seq.append(new_color)
    
    state = "player_move"
    
def Move():
    global state, seq, i
    
    if start_Button.value() == 0:
        state = "waves"        
    

while True:
    if state == "wait":     
        Wait()
    elif state == "start":
        Start()
    elif state == "waves":
        Waves()
    elif state == "player_move":
        Move()
        
