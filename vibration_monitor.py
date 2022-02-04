import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial as sr

plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.ion()   
plt.show()

# Setting up serial connection
s = sr.Serial('COM3', 9600);
try:
    s.close()
except:
    pass
s.open()

if s.is_open==True:
    print("Using Serial port")

sensor_x = []
sensor_y = []
sensor_z = []
count = 0
max_count = 500



def get_sensor_data():
    global sensor_x, sensor_y, sensor_z
    a = s.readline().decode()
    #print("-"*10)
    #print(a)
    if a == None:
        pass
    else:
        b= a.split()
        x,y,z = b
        sensor_x = np.append(sensor_x, [float(x)])
        sensor_y = np.append(sensor_y, [float(y)])
        sensor_z = np.append(sensor_z, [float(z)])
    return sensor_x, sensor_y, sensor_z

while True:
    while s.in_waiting >0:
        get_sensor_data()
        plt.cla()
        if (count > max_count):
            sensor_x.pop(0)
            sensor_y.pop(0)
            sensor_z.pop(0)
        ax.plot(sensor_x)

        plt.pause(0.0001) # required for update of plot
        count += count

s.close()