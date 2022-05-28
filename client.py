from http import client
from iiot_device import Sensor
import json
import time

''' creation of the class of  HTTPConnection'''
_conn = client.HTTPConnection(host='localhost', port=5000)

''' Creation of an object of the class Sensor'''
s = Sensor()

''' Creation of the JSON that goes to the server'''
h = {'Content-type':'application/json'}



while True:
    
    inclination = s.get_random_number()
    
    data = {
        'id': 1,
        'name': 'David Sensor gyroscope',
        'value': inclination
    }

    json_data = json.dumps(data)
    
    '''Sends data to the server'''
    _conn.request('POST','/devices',json_data, headers=h)
    
    
    _conn.close()
    ''' If the inclination is of the platform is  higher than 15 grades, print the message '''
    if(inclination >= 15):
        print("The platform is very inclined: ", inclination, "°")
    else:
        print("The inclination of the platform is good: ", inclination,"°")
        
    time.sleep(1)