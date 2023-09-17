import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

def main(args=None):
    rclpy.init(args=args)
    node = StopRobot()
    rclpy.spin(node)
    rclpy.shutdown()


class StopRobot(Node):
    def __init__(self):
        super().__init__('stop')
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.stop()
 

    def stop(self):
        """ In the run_loop the robot has a command to stop. After the robot
        stops, the node will shutodown or the user could kill the node."""

        msg = Twist()
        msg.angular.z = 0.0
        msg.linear.x = 0.0
        self.vel_pub.publish(msg)
        


if __name__ == '__main__':
    main()