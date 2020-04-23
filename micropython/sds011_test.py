from machine import UART, sleep
import sds011
uart = UART(1)
uart.init(9600, tx=17, rx=16)
dust_sensor = sds011.SDS011(uart)
while True:
    if dust_sensor.read():
        print('pm2.5', dust_sensor.pm25, 'pm10', dust_sensor.pm10)
    else:
        print('No read')
    sleep(5000)
