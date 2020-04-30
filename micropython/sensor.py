# Write your code here :-)
import time
from machine import I2C, Pin
import si7021
import bmp280
import CCS811
import urequests

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

#print(i2c.scan())
si7021_sensor = si7021.Si7021(i2c)
bmp280_sensor = bmp280.BMP280(i2c)
ccs811_sensor = CCS811.CCS811(i2c)
time.sleep(2)

# from sensor import read_sensors, post_sensors_data
def read_sensors():
    data = {}
    #data['unit_id'],
    #data['registered'],
    data['bmp280_temperature'] = bmp280_sensor.temperature
    data['bmp280_pressure'] = bmp280_sensor.pressure
    data['si7021_temperature'] = si7021_sensor.temperature
    data['si7021_humidity'] = si7021_sensor.relative_humidity

    ccs811_sensor.put_envdata(si7021_sensor.relative_humidity, si7021_sensor.temperature)
    if ccs811_sensor.data_ready():
        data['ccs811_tvoc'] = ccs811_sensor.tVOC
        # TODO: Ta med CO2
    data['sds011_dust'] = 0
    #TODO Ta med PM2.5 og PM10
    return data

def post_sensors_data(data):
        data['unit_id'] = 1
        data['registered'] = ''
        #print('Data som sendes til Flask App:', data)
        header_data = { "content-type": 'application/json; charset=utf-8', "devicetype": '1'}
        r = urequests.post('http://10.13.37.120:5000/api/post_data', json=data, headers=header_data)






