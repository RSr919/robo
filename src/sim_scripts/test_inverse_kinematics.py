import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'kinematics'))

from inverse_kinematics import inverse_kinematics
# from kinematics.inverse_kinematics import inverse_kinematics


# Target end-effector position and orientation
x, y = 0.6, 0.6
phi = np.pi / 2

try:
    theta1, theta2, theta3 = inverse_kinematics(x, y, phi)
    print(f"Theta1: {np.degrees(theta1):.2f}°")
    print(f"Theta2: {np.degrees(theta2):.2f}°")
    print(f"Theta3: {np.degrees(theta3):.2f}°")
except ValueError as e:
    print(f"IK Error: {e}")
