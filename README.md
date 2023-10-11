# comprobo23-warmup-project
## About
This project is a collection of essential robot command, localization, and navigation tools for ROS2.
## Install
We developed this project to run on ROS2 Foxy using Ubuntu 22.04 with some ROS2 packages, including the ROS2 Humble cartographer and navigation2. See below for details.
### ROS2 Foxy
We used ROS2 (Humble Hawksbill) on Ubuntu 22.04 (Jammy Jellyfish)
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

We also used the following packages, which you can install with the following command:

```sudo apt-get update && sudo apt-get install -y {each package, appended with a \ character}```

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

### Source Code
As of September 2023, the homepage for this project is [github/ajevans451/comprobo23-warmup-project](https://github.com/ajevans451/comprobo23-warmup-project).

## Behaviors
For each behavior, describe the problem at a high-level. Include any relevant diagrams that help explain your approach.  Discuss your strategy at a high-level and include any tricky decisions that had to be made to realize a successful implementation.
### Custom Teleop


### Square Drive
The NEATO leverages a timer to drive in a square. Using known angular and linear speeds, the NEATO is able to calculate how far it is turning by keeping track of how long it is turning.

### Wall Following
To detect a wall to follow, the NEATO would use the LiDAR to scan the sides of the NEATO at 90 and 180 degrees to determine if there was a closer wall on its right or left. 
![Diagram of the NEATO examining the distances from it at 45, 135, 225, and 315 degrees](/images/wall_following_diagram.png)
Once it determined which side was closer to a wall, it set itself to either following on the right or on the left. If it was following on the right, it would compare the distances read from the LiDAR for angles 45 and 135, comparing them and adjusting its wheel velocities to keep them equal, and therefore keep itself parallel to the wall. If it was following on the left, it would compare the distance for angles 225 and 315.

### Person Following
When following people, the NEATO would assume the person it was following would be nearby and in front of it, so it would take the LiDAR distance readings for a frontal cone (350-10 degrees), filter out distances that were beyond a certain threshold and set its heading towards that nearest object.

### Obstacle Avoidance
To avoid obstacles, the NEATO would drive forward at whatever its initial orientation was until the LiDAR detected an object that was within the distance threshold. Once it determined there was an obstacle, it would stop and turn 45 degrees clockwise and then check what was immediately in front of itself. If there was no obstacle in its path, it would proceed in that direction around the obstacle; if it detected another obstacle, it would repeat the turning step until there was a clear path.

### Finite State Controller
For the finite state controller, what was the overall behavior. What were the states? What did the robot do in each state? How did you combine and how did you detect when to transition between behaviors?  Consider including a state transition diagram in your writeup.
### Object-Oriented Structure
How was your code structured? Make sure to include a sufficient detail about the object-oriented structure you used for your project.

## Reflection
What if any challenges did you face along the way?
### Room for Improvement
What would you do to improve your project if you had more time?
### Key Takeaways
What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.

## Authors

CJ Hilty [(github)](https://github.com/cjhi) \
AJ Evans [(github)](https://github.com/ajevans451)