import numpy as np

# Link lengths (in meters)
L1 = 0.5
L2 = 0.4
L3 = 0.3

def forward_kinematics(theta1, theta2, theta3):
    """
    Compute (x, y) position of the end-effector based on joint angles.
    Angles should be in radians.
    """
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)

    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    x3 = x2 + L3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3 * np.sin(theta1 + theta2 + theta3)

    return (x3, y3), [(0, 0), (x1, y1), (x2, y2), (x3, y3)]
