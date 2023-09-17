from setuptools import find_packages, setup

package_name = 'warmup_package'

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
    maintainer='aj',
    maintainer_email='aj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'warmup_node = warmup_package.warmup_node:main',
            'teleop = warmup_package.teleop:main'
            #'drive_square = warmup_package.drive_square:main'
            #'wall_follower = warmup_package.wall_follower:main'
            #'person_follower = warmup_package.person_follower:main'
            #'obstacle_avoider = warmup_package.obstacle_avoider:main'
            #'finite_state_controller = warmup_package.finite_state_controller:main'
            #'sphere_marker = warmup_package.sphere_marker:main'
        ],
    },
)
