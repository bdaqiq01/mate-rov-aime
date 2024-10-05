from setuptools import find_packages, setup

package_name = 'underwater_rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='basira',
    maintainer_email='basira@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = underwater_rover.test_node:main",
            "temperature_node = underwater_rover.temperature_sensor:main",
            "thruster_node = underwater_rover.thruster_controller:main",
            "claw_1_node = underwater_rover.servo_claw_1:main",
            "navigator_reader_node = underwater_rover.navigator_reader:main",
            "draw_circle_node = underwater_rover.draw_circle:main",
            "barometer_node = underwater_rover.barometer_node:main",
        ],
    },
)
