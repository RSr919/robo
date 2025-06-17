import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import numpy as np
import math
import time

class PickAndPlaceNode(Node):
    def __init__(self):
        super().__init__('pick_and_place')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.joint_names = ['joint1', 'joint2', 'joint3']
        self.theta = 0.0

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joint_names
        msg.position = [
            math.sin(self.theta),
            math.sin(self.theta / 2),
            math.sin(self.theta / 3)
        ]
        self.publisher_.publish(msg)
        self.theta += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = PickAndPlaceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
