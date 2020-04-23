import time
from machine import I2C, Pin
import si7021
import bmp280
import CCS811

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

#print(i2c.scan())
si7021_sensor = si7021.Si7021(i2c)
bmp280_sensor = bmp280.BMP280(i2c)
ccs811_sensor = CCS811.CCS811(i2c)
time.sleep(2)
#temp_sensor.temperature
#temp_sensor.relative_humidity
while True:
    print('Si7021 Temp:', '{:.2f}'.format(si7021_sensor.temperature), 'Hum:', si7021_sensor.relative_humidity)
    print('BMP280 Temp:', '{:.2f}'.format(bmp280_sensor.temperature), 'Press:', bmp280_sensor.pressure, 'Alt:', bmp280_sensor.altitude)
    ccs811_sensor.put_envdata(si7021_sensor.relative_humidity, si7021_sensor.temperature)
    if ccs811_sensor.data_ready():
        print('CCS811 eCO2:', '{:.2f}'.format(ccs811_sensor.eCO2), 'TVOC:', ccs811_sensor.tVOC)
    time.sleep(1)
