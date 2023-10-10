# comprobo23-warmup-project
## About
This project is a collection of essential robot command, localization, and navigation tools for ROS2.
## Install
We developed this project to run on ROS2 Foxy using Ubuntu 22.04 with some ROS2 packages, including the ROS2 Humble cartographer and navigation2. See below for details.
### ROS2 Foxy
We used ROS2 (Humble Hawksbill) on Ubuntu 22.04 (Jammy Jellyfish)
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

We also used the following packages, which you can install with the following command:

```python
sudo apt-get update && sudo apt-get install -y NAMES-OF-PACKAGES
```
Followed by each of the following packages:

```
ros-humble-gazebo-ros-pkgs \
ros-humble-nav2-bringup \
ros-humble-navigation2  \
ros-humble-camera-info-manager \
ros-humble-cartographer-ros \
ros-humble-cartographer \
ros-humble-gscam \
git \
python3-colcon-common-extensions \
gstreamer1.0-plugins-good \
gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-ugly \
gstreamer1.0-libav gstreamer1.0-tools \
gstreamer1.0-x \
gstreamer1.0-alsa \
gstreamer1.0-gl \
gstreamer1.0-gtk3 \
gstreamer1.0-qt5 \
gstreamer1.0-pulseaudio \
python3-pip \
hping3
```

### Source Code
As of September 2023, the homepage for this project is [github/ajevans451/comprobo23-warmup-project](https://github.com/ajevans451/comprobo23-warmup-project).

### Building the packages
After installing the prerequisites, build the packages with colcon:
```python
colcon-build --symlink-install
``` 

## Behaviors
Most of the behaviors we developed for the warmup project are stored in separate executables. Notable details of each is described
### teleop: Custom Teleoperation
We developed a keyboard-capturing node that will allow you to drive the neato around using the WASD key paradigm rather than the stock K-centered series of keys
	q  w  e
	a  -  d
	z  s  c
  -------------------
    spacebar : STOP
    
    o/p : increase speeds (both linear and angular) by 10%
    k/l : increase linear speed by 10%
    n/m : increase angular speed by 10%

### wall_follower: Wall Following
When placed next to a wall on either its left or its right side, the Neato will follow parallel to the closest wall until it reaches the end, then spin around until it is parallel to the next wall, and repeat.

### Square Drive
The Neato will drive in a square based on a timer.
#### Square Drive Demo Video
[TODO: Peek video goes here] 

### person_follower: Person Following
The neato will turn to and follow the largest visible obstacle in a view window. This view window is 2 meters wide by 1 meter tall, centered with and 0.5 meters away from the front bumper of the Neato. We included a marker topic Publisher that will publish the intended destination of the Neato using rviz2.
### obstalce_avoider: Obstacle Avoidance
The Neato will drive straight until it 

### finite_state_controller: Follows obstacles while 
For the finite state controller, what was the overall behavior. What were the states? What did the robot do in each state? How did you combine and how did you detect when to transition between behaviors?  Consider including a state transition diagram in your writeup.
### Object-Oriented Structure
*AJ*: Can you add the diagram we made before, if you have one? Otherwise the document I sent on Discord will be a good place to create the diagram.


## Reflection
We were successful in the learning objectives of the project. After an unexpected library/school community emergency, we struggled to submit the project. Afterwards, we focused on future course curriculum. Both of our Ubuntu installations required a re-install before we were able to run the simulator, which subjected us to hardware issues at the beginning of our development process.
### Room for Improvement
To improve our project, we would implement a more sophisticated person follower algorithm that ignores stationary obstacles in the view window in favor of a moving obstacle.
### Key Takeaways
What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.

## Authors

CJ Hilty [(github)](https://github.com/cjhi) \
AJ Evans [(github)](https://github.com/ajevans451)