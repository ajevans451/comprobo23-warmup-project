import tty
import select
import sys
import termios

import rospy
from geometry_msgs.msg import TwistStamped

import threading

# this is the git repo with the original turtlesim teleop, i'm trying to make sense of it
# https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py


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

class ThreadPublisher(threading.Thread):
	def __init__(self):
		super(ThreadPublisher, self).__init__()
		self.publisher = rospy.Publisher('cmd_vel', TwistStamped, queue_size = 1)
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		self.th = 0.0
		self.speed = 0.0
		self.turn = 0.0
		self.condition = threading.Condition()
		self.done = False
		#self.timeout = None
		self.start()
		
	def update(self, x, y, z, th, speed, turn):
        	self.condition.acquire()
        	self.x = x
		self.y = y
		self.z = z
		self.th = th
		self.speed = speed
		self.turn = turn
		# Notify publish thread that we have a new message.
		self.condition.notify()
		self.condition.release()
		
	def stop(self):
		self.done = True
		self.update(0, 0, 0, 0, 0, 0)
		self.join()
		
	def run(self):
		twist = TwistStamped()
		twist.header.stamp = rospy.Time.now()
		twist.header.frame_id = twist_frame
		
		while not self.done:
			twist.header.stamp = rospy.Time.now()
			self.condition.acquire()
			#self.condition.wait(self.timeout)
			
			# Copy state into twist message.
			twist.linear.x = self.x * self.speed
			twist.linear.y = 0
			twist.linear.z = 0
			twist.angular.x = 0
			twist.angular.y = 0
			twist.angular.z = self.th * self.turn

			self.condition.release()
			self.publisher.publish(twist)
		
		twist.linear.x = 0
		twist.linear.y = 0
		twist.linear.z = 0
		twist.angular.x = 0
		twist.angular.y = 0
		twist.angular.z = 0
		self.publisher.publish(twist)
		
# skeleton key logger from warmup project assignment
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key
# very similar to teleop_twist_keyboard but less robust

def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)
    
if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	
	rospy.init_node('teleop')
	speed = rospy.get_param("~speed", 0.5)
	turn = rospy.get_param("~turn", 1.0)
	speed_limit = rospy.get_param("~speed_limit", 1000)
	turn_limit = rospy.get_param("~turn_limit", 1000)
	repeat = rospy.get_param("~repeat_rate", 0.0)
	key_timeout = rospy.get_param("~key_timeout", 0.5)
	stamped = rospy.get_param("~stamped", False)
	twist_frame = rospy.get_param("~frame_id", '')
	

	pub_thread = PublishThread(repeat)

	x = 0
	y = 0
	z = 0
	th = 0
	status = 0
	
	try:
		pub_thread.update(x, y, z, th, speed, turn)

		print(txt)
		print(vels(speed,turn))
		while(1):
            key = getKey(settings, key_timeout)
            if key in moveBindings.keys():
                x = directionsBindings[key][0]
                th = directionsBindings[key][1]
            elif key in speedBindings.keys():
                speed = min(speed_limit, speed * speedBindings[key][0])
                turn = min(turn_limit, turn * speedBindings[key][1])
                if speed == speed_limit:
                    print("Linear speed limit reached!")
                if turn == turn_limit:
                    print("Angular speed limit reached!")
                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
		
		
	
key = None

# \x03 is CTRL-C
while key != '\x03':
    key = getKey()
    print(key)

