import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import cos, sin, pi

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-pi / 2, pi / 2, scan.shape[0], endpoint=True)

rx, ry = 1.0, 0.5
ox, oy = 0.2, 0.0

T_robot_global = np.array([[cos(pi / 4), -sin(pi / 4), rx], [sin(pi / 4), cos(pi / 4), ry], [0, 0, 1]])
T_laser_robot = np.array([[cos(pi), -sin(pi), ox], [sin(pi), cos(pi), oy], [0, 0, 1]])

T_laser_global = T_robot_global @ T_laser_robot

# Local Coordinates to Laser
local_points = [scan * np.cos(angle), scan * np.sin(angle)]
x, y = local_points[0], local_points[1]
plt.plot(x, y, '.k', markersize=3)
plt.show()

# Apply the transformation to the scan points
w = np.ones(len(x))
scan_laser = np.array([x, y, w])
scan_global = np.matmul(T_laser_global, scan_laser)
# Plot the laser points
plt.figure()
plt.plot(scan_global[0,:], scan_global[1,:], '.k', markersize=3)


# Plot robot pose in blue
plt.plot(T_robot_global[0, 2], T_robot_global[1, 2], '+b')
# Plot laser pose in red
plt.plot(T_laser_global[0, 2], T_laser_global[1, 2], '+r')

vector = np.array([[0.2], [0.0], [1]])
temp = np.dot(T_robot_global, vector)
plt.plot(temp[0], temp[1], T_robot_global[1, 2], '+b')
plt.show()
# scan_global =