import numpy as np
import matplotlib.pyplot as plt
# from kinematics.forward_kinematics import forward_kinematics
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'kinematics'))
from forward_kinematics import forward_kinematics


# Generate joint angle values
joint_angles = np.linspace(0, np.pi/2, 50)
ee_positions = []

# Simulate a motion path where all joints move together
for t in joint_angles:
    pos, _ = forward_kinematics(t, t/2, t/3)
    ee_positions.append(pos)

# Plotting the trajectory
x_vals, y_vals = zip(*ee_positions)
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='o', label='End-Effector Path')
plt.title("End-Effector Trajectory")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()
