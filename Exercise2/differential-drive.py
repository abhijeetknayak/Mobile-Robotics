import numpy as np
from numpy import sin, cos, pi

def rotation(x, y, theta, v_l, v_r, t, l):
    R = (l / 2) * (v_r + v_l) / (v_r - v_l)
    ang_v = (v_r - v_l) / l
    angle = ang_v * t

    T = np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    icc_x, icc_y = x - R * sin(theta), y + R * cos(theta)

    vector_ = np.array([
        [x - icc_x], [y - icc_y], [theta]
    ])
    vector = np.array([
        [icc_x], [icc_y], [angle]
    ])

    result = T @ vector_ + vector
    return result[0, 0], result[1, 0], result[2, 0]

def translation(theta, v_r, v_l, t, x, y):
    T = np.array([
        [cos(theta), -sin(theta), x],
        [sin(theta), cos(theta), y],
        [0, 0, 1]
    ])
    v = (v_r + v_l) / 2
    dist = v * t

    vector = np.array([[dist], [0], [1]])
    prod = T.dot(vector)
    return prod[0, 0], prod[1, 0]

def differential_drive(x, y, theta, v_l, v_r, t, l):
    """
    :param x: Initial Position x
    :param y: Initial Position y
    :param theta: Initial orientation
    :param v_l: Velocity of left wheel
    :param v_r: Velocity of right wheel
    :param t: Time
    :param l: Length between the two wheels. Will be used only when (v_l or v_r) = 0 or when v_l = -v_r
    :return: New positions and orientation
    """

    # v_l | v_r = 0 ----> Turn
    # v_l = -v_r ----> Inplace Rotation
    x_n = 0
    y_n = 0
    if v_r == v_l:
        x_n, y_n = translation(theta, v_r, v_l, t, x, y)
    else:
        x_n, y_n, theta = rotation(x, y, theta, v_l, v_r, t, l)
    return x_n, y_n, theta

if __name__ == '__main__':
    x, y, theta = 1, 2, pi / 2
    x, y, theta = differential_drive(x, y, theta, 1, -1, pi / 4, 1)  # Oriented along X-Axis
    # print("X: {}, Y: {}, Orientation: {}".format(x, y, theta))

    x, y, theta = differential_drive(x, y, theta, 1, 1, 0.5, 1)  # Movement to (1.5, 2)
    # print("X: {}, Y: {}, Orientation: {}".format(x, y, theta))

    x, y, theta = differential_drive(x, y, theta, -1, 1, pi / 4, 1)  # Oriented along Y-Axis
    # print("X: {}, Y: {}, Orientation: {}".format(x, y, theta))

    # Part a
    # c1 = (v_l = 0.3, v_r = 0.3, t = 3)
    v_l, v_r, t, robot_l = 0.3, 0.3, 3, 0.5
    x, y, theta = differential_drive(x, y, theta, v_l, v_r, t, robot_l)
    print("X: {}, Y: {}, Orientation: {}".format(x, y, np.rad2deg(theta)))

    # Part b
    # c2 = (v_l = 0.1, v_r = -0.1, t = 1)
    v_l, v_r, t, robot_l = 0.1, -0.1, 1, 0.5
    x, y, theta = differential_drive(x, y, theta, v_l, v_r, t, robot_l)
    print("X: {}, Y: {}, Orientation: {}".format(x, y, np.rad2deg(theta)))

    # Part c
    # c3 = (v_l = 0.2, v_r = 0, t = 2)
    v_l, v_r, t, robot_l = 0.2, 0, 2, 0.5
    x, y, theta = differential_drive(x, y, theta, v_l, v_r, t, robot_l)
    print("X: {}, Y: {}, Orientation: {}".format(x, y, (theta)))



