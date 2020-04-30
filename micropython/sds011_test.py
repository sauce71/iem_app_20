from machine import UART, sleep
import sds011
uart = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=12, rx=14, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=5000, timeout_char=2)

dust_sensor = sds011.SDS011(uart)
while True:
    if dust_sensor.read():
        print('pm2.5', dust_sensor.pm25, 'pm10', dust_sensor.pm10)
    else:
        print('No read')
    sleep(2000)
