import numpy as np

def forward_kinematics(theta1, theta2, theta3, a1=5.2, a2=6.9, a3=6.8):
    t1, t2, t3 = np.deg2rad([theta1, theta2, theta3])
    x = a1*np.cos(t1) + a2*np.cos(t1+t2) + a3*np.cos(t1+t2+t3)
    y = a1*np.sin(t1) + a2*np.sin(t1+t2) + a3*np.sin(t1+t2+t3)
    return x, y
