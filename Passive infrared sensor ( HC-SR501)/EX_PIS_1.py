from machine import Pin
from utime import sleep

sensor = Pin(28, Pin.IN)
led = Pin(15, Pin.OUT)
def pir_handler(pin):
    print('ALARM')
    for i in range(50):
        led.toggle()
        sleep(0.1)
sensor.irq(trigger  = Pin.IRQ_RISING, handler = pir_handler)
while True:
    led.value(0)