from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
led = LED(14)

## GUI Definitions
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## event funktion
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "   Turn LED on   "
    else:
        led.on()
        ledButton["text"] = "   Turn LED off   "

def ledToggle2():
    print ("Tryk")

## Widgets
ledButton = Button(win, text = 'turn led on', font = myFont, comman = ledToggle)
ledButton.grid(row=0,column=1)

ledButton2 = Button(win, text = 'Test 2', font = myFont, comman = ledToggle2)
ledButton2.grid(row=1,column=1)
