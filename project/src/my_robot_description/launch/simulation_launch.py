from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=['urdf/three_dof_arm.urdf']
        ),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
        )
    ])
