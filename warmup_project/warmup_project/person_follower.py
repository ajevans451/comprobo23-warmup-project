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
from visualization_msgs.msg import Marker

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

class SimpleVisualizationPublisher(Node):
    def __init__(self):
        super().__init__('test_vis')
        self.vis_pub = self.create_publisher(Marker, 'visualization_marker', 10)

        timer_period = 0.1 #  rate of 10x / second
        self.timer = self.create_timer(timer_period, self.publish_marker)
    
    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = "base_link";
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "my_namespace";
        marker.id = 0

        marker.type = Marker.SPHERE;
        marker.action = Marker.ADD;
        marker.pose.position.x = 1.0
        marker.pose.position.y = 2.0
        marker.pose.position.z = 1.0
        marker.pose.orientation.x = 6.9;
        marker.pose.orientation.y = 42.0;
        marker.pose.orientation.z = 0.0;
        marker.pose.orientation.w = 1.0;
        marker.scale.x = 1.0
        marker.scale.y = 0.1
        marker.scale.z = 0.1
        marker.color.a = 0.9; # Don't forget to set the alpha!
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 1.0

        self.vis_pub.publish( marker );

def main(args=None):
    rclpy.init(args=args)

    simple_visualization_publisher = SimpleVisualizationPublisher()

    rclpy.spin(simple_visualization_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    simple_visualization_publisher.destroy_node()
    rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    follower = PersonFollower() # This initiates a lidar-subscribing timer
    print("Node Initiated.")
    rclpy.spin(follower)
    rclpy.shutdown()

if __name__ == '__main__':
    main()