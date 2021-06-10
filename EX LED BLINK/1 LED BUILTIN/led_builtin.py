from machine import Pin
from time import sleep
LED_BUILTIN = Pin(25, Pin.OUT)
while True:
    LED_BUILTIN.high()
    sleep(1)
    LED_BUILTIN.low()
    sleep(1)