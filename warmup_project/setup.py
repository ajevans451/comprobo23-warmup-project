from setuptools import find_packages, setup

package_name = 'warmup_project'

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
    maintainer='cjhi',
    maintainer_email='chilty@olin.edu',
    description='Features for the CompRobo warmup project at Olin College,\
                comprobo23.github.io/',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop = warmup_project.teleop:main',
            'drive_square = warmup_project.drive_square:main',
            'finite_state_controller = finite_state_controller.teleop:main',
            'wall_follower = warmup_project.wall_follower:main',
            'obstacle_avoider = obstacle_avoider.teleop:main',
            'person_follower = person_follower.teleop:main',
            'stop = warmup_project.stop:main',
        ],
    },
)