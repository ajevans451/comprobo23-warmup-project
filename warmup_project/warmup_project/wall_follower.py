#Node and robot command boilerplate
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
from sensor_msgs.msg import LaserScan

# #Keyboard capture
# import tty
# import select
# import sys
# import termios
# settings = termios.tcgetattr(sys.stdin)

class WallFollower(Node):
    def __init__(self):
        super().__init__("teleop")
        self.sub = self.create_subscription(LaserScan, 'scan', self.readLidar, 10)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_timer(0.1,self.runLoop)
        self.scanValues = []
        WheelOutput = [0.5 0] #[linear angular]. Linear: positive is forward, negative is backwards. Angular: positive is counterclockwise, negative is clockwise.
        self.FollowingLeft=True

def ChooseSide(LaserScan):
    ''' Returns which side the neato is probably following a wall on. We assume that if the wall is on the left, measurements from the right will be further away than the left.'''
    pass #FollowingLeft = LaserScan[d180] < LaserScan[d0] #will be true if the 180-degree left hand size is closer.
    return FollowingLeft

def OrientToWall(self):
    """ outputs the wheel velocities needed to make the robot get closer to following the wall."""

    if FollowingLeft:
        if ahead > behind # AKA 45 and d135
            turnAmount = ahead/behind
        elif ahead < behind
            turnAmount = -1*behind/ahead
        else:
            turnAmount = 0
    else: #following a wall to the right
        if ahead > behind #and here, AKA 225 and d315
            turnAmount = -ahead/behind
        elif ahead < behind
            turnAmount = behind/ahead
        else:
            turnAmount = 0
    return turnAmount

def readLidar(self, msg):
    angles = [90, 180, 45, 135, 225, 315]
    self.scanValues = [] # Should give an empty list for appending
    if msg.ranges.includes(0):
        pass # TODO: FIRST: add print statements and make the node runnable. Get ride of pseudocode and just make it run. See where the data tyeps print.
    # SECOND: GET LIDAR SCANS THAT ARE GOOD, which means they don't have 0s in the 45 etc ranges that we care about.
    # THIRD, add a proportional multiplier to the output of the angular output commands. Test the neato.
    else:
        for value in angles:
            self.scanValues.append(msg.ranges[value]) #Should leave us with a 6-element list

def runLoop(self):
    FollowingLeft = ChooseSide(LaserScan)
    WheelOutput[0] = OrientToWall(LaserScan, FollowingLeft)
    Twist.publish(WheelOutput)
    
def main(args=None):
    rclpy.init(args=args)
    wally = WallFollower() # This initiates a lidar-subscribing timer
    print("Node Initiated.")
    rclpy.spin(wally)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
