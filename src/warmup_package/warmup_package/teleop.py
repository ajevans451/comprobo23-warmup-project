import tty
import select
import sys
import termios
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



# skeleton key logger from warmup project assignment
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key
# very similar to teleop_twist_keyboard but less robust


settings = termios.tcgetattr(sys.stdin)
key = None

# \x03 is CTRL-C
while key != '\x03':
    key = getKey()
    print(key)

