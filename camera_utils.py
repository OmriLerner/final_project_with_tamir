import numpy as np
import cv2
import math
from math import sin, cos

deg2rad = math.pi/180
camera_mat = np.array([ [463.84660267,   0.0,         346.06712511]
                        [  0.0,         462.83399024, 249.21266182]
                        [  0.0,           0.0,           1.0        ]])

distortion_params = np.array([-0.40287713,  0.20543671,  0.00040524, -0.00206542, -0.06366589])


yaw_error = 20*deg2rad

yaw_rotation_mat = np.array([[cos(yaw_error, 0, sin(yaw_error))],
                             [0, 1, 0], 
                             [-sin(yaw_error), 0, cos(yaw_error)]])


def get_angle(tag_center):
    fixed_center = cv2.undistortPoints(tag_center, camera_mat, distortion_params, R=yaw_rotation_mat)[0][0]
    angles = (math.atan(fixed_center[0]), math.atan(fixed_center[1]))
    return angles

