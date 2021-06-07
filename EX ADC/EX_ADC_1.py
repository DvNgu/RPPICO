from machine import ADC
from time import sleep
adc = ADC(26)

while True:
    value = adc.read_u16()
    voltage = (value * 3.3) / 65535
    print('='*20)
    print('analog  = ', value)
    print("voltage = ", voltage)
    sleep(0.5)
    