#Node and robot command boilerplate
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#Keyboard capture
import tty
import select
import sys
import termios

# the instructions message for easy usage (unlike the original, we dont have z or strafing)

txt = """
    Moving around:
	q  w  e
	a  -  d
	z  s  c
  -------------------
    other keys : STOP
    
    o/p : increase speeds (both linear and angular) by 10%
    k/l : increase linear speed by 10%
    n/m : increase angular speed by 10%
    
    CTRL-C to QUIT
"""

class Teleop(Node):
    def __init__(self):
        super().__init__('stop')
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.lin_scale = 1.0
        self.ang_scale = 1.0
        self.lin_dir = 0
        self.ang_dir = 0
        self.create_timer(0.1,self.run_loop())

        self.directionBindings = {
        # affixing the key/value pair to a list with only 2 values (linear direction/turn direction) might be a mistake if we're intended to leverage the existing Twist msgs but i'm trying it anyway
        'q':(1,1), 
        'w':(1,0),
        'e':(1,-1),
        'a':(0,1),
        'd':(0,-1),
        'z':(-1,1),
        's':(-1,0),
        'c':(-1,-1),
        ' ':(0,0)
        }
        self.speedBindings = {
        # these key/value pairs are nearly identical
	    'o':(1.1,1.1),
        'p':(.9,.9),
        'k':(1.1,1),
        'l':(.9,1),
        'n':(1,1.1),
        'm':(1,.9),
        }

# skeleton key logger from warmup project assignment
def getKey():
        print(key)
        key = None
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key
def vels(speed,turn):
    print(f"Speed is {speed} and turn is {turn}.")

    def update_velocity(self):
        """ This docstring is incorrect."""
        msg = Twist() #Get the message formatted with the neato speeds
        key = getKey()
        if key in self.speedBindings.keys():
            self.lin_scale = self.lin_scale * self.speedBindings(key(1))
            self.ang_scale = self.ang_scale * self.speedBindings(key(2))
        if key in self.directionBindings.keys():
             self.lin_dir = self.directionBindings(key(1))
             self.ang_dir = self.directionBindings(key(2))
        msg.linear.x = self.directionBindings(key(1))*self.lin_scale
        msg.angular.z = self.directionBindings(key(2))*self.ang_scale
        self.vel_pub.publish(msg) #pub changes after setting the values in the twist message

    def run_loop(self):
        self.update_velocity()
        vels(self.lin_scale,self.ang_scale)

        
def main(args=None):
    rclpy.init(args=args)
    node = Teleop()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
