import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from kinematics.forward_kinematics import forward_kinematics
from kinematics.inverse_kinematics import inverse_kinematics

# Define pick and place points
start_xy = (0.4, 0.3)
end_xy = (0.6, 0.8)
phi = np.pi / 2  # end-effector pointing up

# Generate trajectory linearly in task space
num_frames = 50
x_vals = np.linspace(start_xy[0], end_xy[0], num_frames)
y_vals = np.linspace(start_xy[1], end_xy[1], num_frames)

# Solve inverse kinematics for each (x, y)
joint_trajectories = []
for x, y in zip(x_vals, y_vals):
    try:
        thetas = inverse_kinematics(x, y, phi)
        joint_trajectories.append(thetas)
    except ValueError:
        joint_trajectories.append(None)

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 1.5)
ax.set_aspect('equal')
ax.set_title("Pick and Place Animation")
line, = ax.plot([], [], 'o-', lw=3)

# Animation function
def animate(i):
    line.set_data([], [])
    angles = joint_trajectories[i]
    if angles is None:
        return line,

    _, points = forward_kinematics(*angles)
    xs, ys = zip(*points)
    line.set_data(xs, ys)
    return line,

# Run animation
ani = FuncAnimation(fig, animate, frames=len(joint_trajectories), interval=100)
plt.show()
