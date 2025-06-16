import numpy as np

# Link lengths
L1 = 0.5
L2 = 0.4
L3 = 0.3

def inverse_kinematics(x, y, phi):
    """
    Compute inverse kinematics for planar 3-DOF arm.
    phi = desired end-effector orientation (radians)
    Returns theta1, theta2, theta3 (in radians)
    """
    # Compute wrist position
    wx = x - L3 * np.cos(phi)
    wy = y - L3 * np.sin(phi)

    # Compute theta2
    D = (wx**2 + wy**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(D) > 1:
        raise ValueError("Target not reachable")

    theta2 = np.arctan2(np.sqrt(1 - D**2), D)  # elbow down
    # theta2 = np.arctan2(-np.sqrt(1 - D**2), D)  # elbow up (optional)

    # Compute theta1
    s2 = np.sin(theta2)
    c2 = np.cos(theta2)

    k1 = L1 + L2 * c2
    k2 = L2 * s2

    theta1 = np.arctan2(wy, wx) - np.arctan2(k2, k1)

    # Compute theta3
    theta3 = phi - theta1 - theta2

    return theta1, theta2, theta3
