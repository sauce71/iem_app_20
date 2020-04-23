import requests
from random import randint
from datetime import datetime


for n in range(100):
    data = {}
    data['unit_id'] = 1
    #data['registered'] = str(datetime.now())
    dt = datetime.now()
    dt = dt.replace(day=randint(1,30))
    # TODO: Utvid med feltene til sensorene deres
    data['registered'] = str(dt)    
    data['bmp280_temperature'] = randint(20,30)
    data['bmp280_pressure'] = randint(950, 1100)
    data['si7021_temperature'] = randint(950, 1100)
    data['si7021_humidity'] = randint(950, 1100)
    data['ccs811_tvoc'] = randint(950, 1100)
    data['sds011_dust'] = randint(950, 1100)
    #print('Data som sendes til Flask App:', data)
    r = requests.post('http://127.0.0.1:5000/api/post_data', json=data)
    print(r.text)
    