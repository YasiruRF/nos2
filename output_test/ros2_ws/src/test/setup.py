from setuptools import find_packages, setup

package_name = 'test'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/' + f for f in []]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='NOS',
    maintainer_email='nos@local',
    description='Auto-generated ROS2 package from NOS',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_node_node = test.simple_node_node:main',
        ],
    },
)
