#split all ranges into 10/15 degree chunks
#take mean of each chunk
# find standard deviation of each chunk



# filter out chunks that are too far (mean too big)
# filter out chunks that are not one objection (stdev too big)

# alternatively: scan things ahead of the neato (350-10 degrees)
# and filter out objects that are too far, take the heading of the closest thing and head there

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
from sensor_msgs.msg import LaserScan

class PersonFollower(Node):
    def __init__(self):
        super().__init__("teleop")
        self.create_subscription(LaserScan, 'scan', self.readLidar, 10)
        # bump
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_timer(0.1,self.runLoop)
        self.scanValues = []
        self.wheelOutput = [0.5, 0] #[linear angular]. Linear: positive is forward, negative is backwards. Angular: positive is counterclockwise, negative is clockwise.

    def OrientToPerson(self):
        """ outputs the wheel velocities needed to make the robot turn towards the person it's following"""
        pass

    def readLidar(self, msg):
        # discard readings that are too far or zero
        # take average of ranges 350-10
        pass


    def updateVelocity(self):
        vels = Twist()
        vels.linear.x = self.wheelOutput[0]
        vels.angular.z = self.wheelOutput[1]
        self.vel_pub.publish(vels)

    def runLoop(self):
        self.FollowingLeft = self.readLidar()
        self.wheelOutput[0] = self.OrientToWall(LaserScan)
        self.setVelocity() #Set values for the twist object
    
def main(args=None):
    rclpy.init(args=args)
    follower = PersonFollower() # This initiates a lidar-subscribing timer
    print("Node Initiated.")
    rclpy.spin(follower)
    rclpy.shutdown()

if __name__ == '__main__':
    main()