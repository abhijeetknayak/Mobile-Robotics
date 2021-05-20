import numpy as np
import math
import matplotlib.pyplot as plt

PLOT = 1

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(3 * np.pi / 2, np.pi / 2, scan.shape[0], endpoint=True)

if PLOT:
    fig = plt.figure()
    ax = fig.gca(polar=True)
    ax.plot(angle, scan)
    plt.savefig('laserscan.jpg')
    plt.show()

    # plt.polar(angle, scan)
    # plt.show()

offset_x = 0.2

# Global Coordinates in CAPITALS
ROBOT_X, ROBOT_Y = 1.0, 0.5


def rotate_translate(theta, px, py, tx, ty):
    hom_matrix = np.array([[np.cos(theta), -np.sin(theta), tx], [np.sin(theta), np.cos(theta), ty], [0, 0, 1]])
    vector = np.array([[px], [py], [1]])  # Column Vector
    return np.dot(hom_matrix, vector)

def find_laserscanner_coordinates():
    return rotate_translate(np.pi / 4, ROBOT_X, ROBOT_Y, offset_x, 0.0)

def global_coordinates():
    find_laserscanner_coordinates()
    local_points = [scan * np.cos(angle), scan * np.sin(angle)]
    LASERSCAN = find_laserscanner_coordinates()

    if PLOT:
        plt.scatter(local_points[0], local_points[1])
        plt.plot(ROBOT_X, ROBOT_Y, 'bo')
        plt.plot(LASERSCAN[0], LASERSCAN[1], 'ro')
        plt.savefig('LaserScans-Robot-Perspective.jpg')
        plt.show()

    for idx in range(0, len(local_points[0])):
        temp = rotate_translate(0, local_points[0][idx], local_points[1][idx], -offset_x, 0.0)
        temp = rotate_translate(np.pi / 4, temp[0], temp[1], -ROBOT_X, -ROBOT_Y)
        local_points[0][idx], local_points[1][idx] = temp[0], temp[1]

    if PLOT:
        plt.scatter(local_points[0], local_points[1])
        plt.plot(ROBOT_X, ROBOT_Y, 'bo')
        plt.plot(LASERSCAN[0], LASERSCAN[1], 'ro')
        plt.savefig("LaserScans-Global-Perspective.jpg")
        plt.show()


if __name__ == '__main__':
    global_coordinates()


