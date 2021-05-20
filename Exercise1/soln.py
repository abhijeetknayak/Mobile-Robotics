import numpy as np
import matplotlib.pyplot as plt
import pdb
pi = np.pi
# a) Load laserscan and plot in scanner frame
#pdb.set_trace()
scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-pi/2, pi/2, np.shape(scan)[0], endpoint=True)
x = scan * np.cos(angle)
y = scan * np.sin(angle)
plt.plot(x, y, '.k', markersize=3)
#for i in range(len(x)):
# plt.plot([0, x[i]], [0,y[i]], color=’r’)
# Set the same scale on both axes
plt.gca().set_aspect('equal')
plt.savefig('scan1.pdf')
# c) Transform to global frame
# Define the transformation matrices
T_global_robot = np.array(
[[np.cos(pi/4), -np.sin(pi/4), 1],
[np.sin(pi/4), np.cos(pi/4), 0.5],
[0, 0, 1]])
T_robot_laser = np.array(
[[np.cos(pi), -np.sin(pi), 0.2],
[np.sin(pi), np.cos(pi), 0.0],
[0, 0, 1]])
# Compute the laser frame w.r.t. the global frame
T_global_laser = np.matmul(T_global_robot, T_robot_laser)
# Apply the transformation to the scan points
w = np.ones(len(x))
scan_laser = np.array([x, y, w])
scan_global = np.matmul(T_global_laser, scan_laser)
# Plot the laser points
plt.figure()
plt.plot(scan_global[0,:], scan_global[1,:], '.k', markersize=3)
# Plot robot pose in blue
plt.plot(T_global_robot[0,2], T_global_robot[1,2], '+b')
# Plot laser pose in red
plt.plot(T_global_laser[0,2], T_global_laser[1,2], '+r')
# Set the same scale on both axes
plt.gca().set_aspect('equal')
plt.show()
#plt.savefig(’scan2.pdf’)