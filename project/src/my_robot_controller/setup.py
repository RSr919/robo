from setuptools import setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='Publishes joint states to animate 3DOF robot arm',
    license='MIT',
    entry_points={
        'console_scripts': [
            'pick_and_place_anim = my_robot_controller.pick_and_place_anim:main',
        ],
    },
)
