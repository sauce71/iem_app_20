import urequests
from random import randint

#from test_post_fra_esp import test


def test():
    for n in range(10):
        data = {}
        data['unit_id'] = 1
        #data['registered'] = str(datetime.now())
        #dt = datetime.now()
        #dt = dt.replace(day=randint(1,30))
        # TODO: Utvid med feltene til sensorene deres
        day=str(randint(10,30))
        hour = str(randint(10,23))
        minutes = str(randint(10,59))
        data['registered'] = '2020-04-{} {}:{}:51.608730'.format(day, hour, minutes)
        data['bmp280_temperature'] = randint(20,30)
        data['bmp280_pressure'] = randint(950, 1100)
        data['si7021_temperature'] = randint(950, 1100)
        data['si7021_humidity'] = randint(950, 1100)
        data['ccs811_tvoc'] = randint(950, 1100)
        data['sds011_dust'] = randint(950, 1100)
        #print('Data som sendes til Flask App:', data)
        header_data = { "content-type": 'application/json; charset=utf-8', "devicetype": '1'}
        r = urequests.post('http://10.13.37.120:5000/api/post_data', json=data, headers=header_data)
        print(r.text)

