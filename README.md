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

Followed by each of the following packages:

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
Most of the behaviors we developed for the warmup project are stored in separate executables. Notable details of each are described below.

### teleop: Custom Teleoperation

We developed a keyboard-capturing node that will allow you to drive the NEATO around using the WASD key paradigm rather than the stock K-centered series of keys.
```python 
	q  w  e
	a  -  d
	z  s  c

    spacebar : STOP
    
    o/p : increase speeds (both linear and angular) by 10%
    k/l : increase linear speed by 10%
    n/m : increase angular speed by 10%
```

### drive_square: Square Drive
The NEATO leverages a timer to drive in a square. Using known angular and linear speeds, the NEATO is able to calculate how far it is turning by keeping track of how long it is turning.

#### Square Drive Demo Video
![drive_square Demo](/Screenshots/drive_square.gif)

### wall_follower: Wall Following
To detect a wall to follow, the NEATO will use the LiDAR to scan the sides of the NEATO at 90 and 180 degrees to determine if there was a closer wall on its right or left. 
![Diagram of the NEATO examining the distances from it at 45, 135, 225, and 315 degrees](/images/wall_following_diagram.png)
Once it determined which side was closer to a wall, it set itself to either following on the right or on the left. If it was following on the right, it will compare the distances read from the LiDAR for angles 45 and 135, comparing them and adjusting its wheel velocities to keep them equal, and therefore keep itself parallel to the wall. If it was following on the left, it will compare the distance for angles 225 and 315.

### person_follower: Person Following
When following people, the NEATO will assume the person it was following will be nearby and in front of it, so it will take the LiDAR distance readings for a frontal cone (350-10 degrees), filter out distances that were beyond a certain threshold and set its heading towards that nearest object. It will stop once it is 0.5 meters away from the front bumper of the neato. We included a Marker topic Publisher that will publish the intended location of the Neato, viewable using rviz2.

### obstacle_avoider: Obstacle Avoidance
The NEATO will have a goal location to attain. If it encounters an obstacle on the way to that goal, it will then give a 0.25 meter berth to that obstacle and travel as close as possible to the goal location. Like in person_follower, we include a Publisher that will publish the intended next location of the Neato using rviz2. To avoid obstacles, the NEATO will drive forward at whatever its initial orientation was until the LiDAR detected an object that was within the distance threshold. Once it determined there was an obstacle, it will stop and turn 45 degrees clockwise and then check what was immediately in front of itself. If there was no obstacle in its path, it will proceed in that direction around the obstacle; if it detected another obstacle, it will repeat the turning step until there was a clear path.

### finite_state_controller: Explores and Follows People 
Our finite state controller will initialize by having the NEATO wander in a square. If the NEATO detects a wall first, it will follow the wall until it detects a person. Once the NEATO detects a person, it will follow the person. If the person runs away, the NEATO will just go back to drive in a square. If it is still near a wall, it will begin following the wall until it finds another person to follow, and the cycle repeats.

![Finite-State Machine Diagram](/images/fsm.jpg)

### stop: Convenient Halt Command
This no-frills module will send a single stop command to the NEATO, then shut down.

### Object-Oriented Structure
Each node is initially defined in its own .py file. Each file defines classes, so multiple instances of the same class can run at one time.

## Reflection
We were successful in the learning objectives of the project. After an unexpected library/school community emergency, we struggled to submit the project. Afterwards, we focused on future course curriculum. Both of our Ubuntu installations required a re-install before we were able to run the simulator, which subjected us to hardware issues at the beginning of our development process.
### Room for Improvement
To improve our project, we will implement a more sophisticated person follower algorithm that ignores stationary obstacles in the view window in favor of a moving obstacle.
### Key Takeaways
What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.

## Authors

CJ Hilty [(github)](https://github.com/cjhi) \
AJ Evans [(github)](https://github.com/ajevans451)