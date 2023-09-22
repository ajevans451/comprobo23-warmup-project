#Use Ranges
#move forward (0) until too close to obstacle

# get lidar scan -- if ranges[0] is < distance_threshold: stop, turn 45 degrees left, check ranges[0] again, if < distance_threshold, turn 45 degrees right (from original heading), check ranges[0]
# if < distance_threshold, repeat process in intervals of 15/30/45 degrees until the way is clear, then drive forward with new bearing for some time
# reorient to odom 0, check for obstacle at ranges[0] again
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
from sensor_msgs.msg import LaserScan

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__("teleop")
        self.create_subscription(LaserScan, 'scan', self.readLidar, 10)
        # bump
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_timer(0.1,self.runLoop)
        self.scanValues = []
        self.wheelOutput = [0.5, 0] #[linear angular]. Linear: positive is forward, negative is backwards. Angular: positive is counterclockwise, negative is clockwise.

    def readLidar(self, msg):
        # check for zeros
        # check for values within 0.5m in angles 355-5, if found throw object found
        # 
        pass

    
def main(args=None):
    rclpy.init(args=args)
    print("Node Initiated.")
    dodger = ObstacleAvoider() # This initiates a lidar-subscribing timer
    rclpy.spin(dodger)
    rclpy.shutdown()

if __name__ == '__main__':
    main()