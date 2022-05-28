<<<<<<< HEAD
=======
##libraries
>>>>>>> master
from random import randint
import psutil


# POO en Python

'''Class definition'''
class Sensor:
    
    '''Class constructor'''
    def __init__(self):
        self._sensor = psutil.cpu_stats() 
         
    def get_temp(self):
        return self._sensor['coretemp']
    
    ''' It simulates the take of values of another sensor '''
    def get_random_number(self):
        return randint(0, 90)
