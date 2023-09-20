#Node and robot command boilerplate
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#Keyboard capture
import tty
import select
import sys
import termios
settings = termios.tcgetattr(sys.stdin)


# the instructions message for easy usage (unlike the original, we dont have z or strafing)

txt = """
    Moving around is WASD-focused. Use
	q  w  e
	a  -  d
	z  s  c
  -------------------
    spacebar : STOP
    
    o/p : increase speeds (both linear and angular) by 10%
    k/l : increase linear speed by 10%
    n/m : increase angular speed by 10%
    
    CTRL-C to QUIT
"""
def getKey():
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

def vels(speed,turn):
    print(f"Linear Speed is {speed} and Angular Speed is {turn}.")


directionBindings = {
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
speedBindings = {
    # these key/value pairs are nearly identical
    'o':(1.1,1.1),
    'p':(.9,.9),
    'k':(1.1,1),
    'l':(.9,1),
    'n':(1,1.1),
    'm':(1,.9),
    }

class Teleop(Node):
    def __init__(self):
        super().__init__("teleop")
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.lin_scale = 1.0
        self.ang_scale = 1.0
        self.lin_dir = 0
        self.ang_dir = 0
        print(txt)

    def update_velocity(self):
        """Updates the velocity, linear and angular."""
        key = None
        msg = Twist() #Get the message formatted with the speeds
        while key != '\x03':
            key = getKey()
            if key in speedBindings.keys(): #.keys() is the native dictionary key ennumerator in python
                self.lin_scale = self.lin_scale * speedBindings[key][0]
                self.ang_scale = self.ang_scale * speedBindings[key][1]
                vels(self.lin_scale,self.ang_scale)

            elif key in directionBindings.keys():
                self.lin_dir = directionBindings[key][0]
                self.ang_dir = directionBindings[key][1]

            # blin.der haha funny joke
            msg.linear.x = self.lin_dir*self.lin_scale
            msg.angular.z = self.ang_dir*self.ang_scale
            self.vel_pub.publish(msg) #pub changes after setting the values in the twist message
    def run_loop(self):
        self.update_velocity()

def main(args=None):
    rclpy.init(args=args)
    print("Node Initiated.")
    Tnode = Teleop()
    Tnode.create_timer(0.1,Tnode.run_loop())
    rclpy.spin(Tnode)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
