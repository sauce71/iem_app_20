import urequests
header_data = { "content-type": 'application/json; charset=utf-8', "devicetype": '1'}
r = urequests.post('http://192.168.68.119:5000/api/test', json={'data':5}, headers=header_data)
