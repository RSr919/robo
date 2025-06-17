from forward_kinematics import forward_kinematics

angles = [(30, 45, 60), (45, 30, 15), (60, 60, -30)]

for theta1, theta2, theta3 in angles:
    x, y = forward_kinematics(theta1, theta2, theta3)
    print(f"Joint angles: {theta1}, {theta2}, {theta3} => End-effector: ({x:.2f}, {y:.2f})")
