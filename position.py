import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

names = ['t', 'gyro', 'wr', 'wl']
data = pd.read_csv('./data.csv', names=names, header = 0, engine='python', index_col=False)

r = 55/2
b = 120

x = 0
y = 0
theta = 0

totalResult = np.matrix([x, y, theta])

for i in range(1, len(data)-1):
    x_cur = x
    y_cur = y
    theta_cur = theta
    dsl = (data['wl'][i] - data['wl'][i - 1]) * r
    dsr = (data['wr'][i] - data['wr'][i - 1]) * r
    x = x_cur + ((dsl + dsr)/2)*math.cos(theta + (dsr-dsl)/(2*b))
    y = y_cur + ((dsl + dsr)/2)*math.sin(theta + (dsr-dsl)/(2*b))
    theta = theta_cur + (dsr-dsl)/b
    
    totalResult = np.append(totalResult, [[x, y, theta]], axis=0)
    
plt.plot(np.squeeze(np.asarray(totalResult[:,0])), np.squeeze(np.asarray(totalResult[:,1])), lw=1)
plt.title("Path without Kalman filter")
plt.tight_layout()
plt.savefig('./pathWithoutKalman.jpg', format='jpg')
plt.show() 

plt.plot(totalResult[:,2]*180/np.pi, lw=1)
plt.title("Rotation using theta")
plt.tight_layout()
plt.savefig('./rotTheta.jpg', format='jpg')
plt.show() 

plt.plot(data['gyro'], lw=1)
plt.title("Rotation using gyro")
plt.tight_layout()
plt.savefig('./rotGyro.jpg', format='jpg')
plt.show() 