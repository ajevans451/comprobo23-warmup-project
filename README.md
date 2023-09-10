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
### Wall Following
### Square Drive
### Person Following
### Obstacle Avoidance
### Finite State Controller
For the finite state controller, what was the overall behavior. What were the states? What did the robot do in each state? How did you combine and how did you detect when to transition between behaviors?  Consider including a state transition diagram in your writeup.
### Object-Oriented Structure
How was your code structured? Make sure to include a sufficient detail about the object-oriented structure you used for your project.
#### foo 

#### bar

## Reflection
What if any challenges did you face along the way?
### Room for Improvement
What would you do to improve your project if you had more time?
### Key Takeaways
What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.
#### foo

#### Barbie

## Authors

CJ Hilty [(github)](https://github.com/cjhi) \
AJ Evans [(github)](https://github.com/ajevans451)