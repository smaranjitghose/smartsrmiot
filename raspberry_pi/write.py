#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
    text = input('Enter data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Data Written")
finally:
    GPIO.cleanup()
