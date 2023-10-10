#Node and robot command boilerplate
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import statistics
from sensor_msgs.msg import LaserScan
from array import array

class WallFollower(Node):
    def __init__(self):
        super().__init__("teleop")
        self.create_subscription(LaserScan, 'scan', self.readLidar, 10)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_timer(0.1,self.runLoop)
        self.scanValues = []
        self.wheelOutput = [0.5, 0] #[linear angular]. Linear: positive is forward, negative is backwards. \
                                    # Angular: positive is counterclockwise, negative is clockwise.
        self.angles = [90, 270, 45, 135, 225, 315, 0]
        self.kp = 0.5
        self.followingLeft = True

    def TrackWall(self):
        """ outputs the wheel velocities needed to make the robot get closer to following the wall."""
        turnAmount = float(0)
        distance = self.scanValues

        if self.scanValues != []:
            print(f"scan values are {distance}")
            if self.followingLeft == True:
                #comparing 45 and 135 (front and back)
                if abs(distance[2]-distance[3]) < 0.01:
                    turnAmount = 0
                elif distance[2] > distance[3]:
                    turnAmount = (abs(distance[2]-distance[3]))
                elif distance[2] < distance[3]:
                    turnAmount = -1*(abs(distance[3]-distance[2]))
                else:
                    turnAmount = 0
            else:
                #comparing 315 and 225
                if abs(distance[5]-distance[4]) < 0.01:
                    turnAmount = 0
                elif distance[5] > distance[4]:
                    turnAmount = -1*abs(distance[5]-distance[4])
                elif distance[5] < distance[4]:
                    turnAmount = abs(distance[4]-distance[5])
                else:
                    turnAmount = 0
        return turnAmount

    def ChooseSide(self):
        ''' Returns which side the neato is probably following a wall on.
            We assume that if the wall is on the left, measurements from the
            right will be further away than the left.'''
        if self.scanValues == []: # Lidar isn't an array yet.
            pass
        elif abs(self.scanValues[0] - self.scanValues[1]) < 0.1:
            self.followingLeft = True
        elif self.scanValues[0] >= self.scanValues[1]:
            self.followingLeft = True #will be true if the LHS distance is closer.
        else: #RHS wall is closer
            self.followingLeft = False
        print(self.followingLeft)

    def readLidar(self, msg):
        #print(type(msg.ranges))
        if isinstance(msg.ranges,array):
            print("array found")
            self.scanValues.clear() # Should give an empty list for appending
            for value in self.angles:
<<<<<<< HEAD
                #average 5 distances around angles of interest
                avg = statistics.mean([msg.ranges[value - 2],msg.ranges[value - 1], msg.ranges[value], msg.ranges[value + 1], msg.ranges[value + 2]])
                self.scanValues.append(avg) #Should leave us with a 6-element list
=======
                print(f"value is {msg.ranges[value]}")
                if msg.ranges[value] >= 0.05 and msg.ranges[value] <= 50:
                    self.scanValues.append(msg.ranges[value]) #Should leave us with a 6-element list
                else:
                    print("Scan rejected")
>>>>>>> 7eeb82c05b55d170f63a12deac4610f8fda221fb
        else:
            print("Lidar wasn't an array")

    def updateVelocity(self):
        vels = Twist()
        vels.linear.x = self.wheelOutput[0]
        vels.angular.z = self.wheelOutput[1]
        self.vel_pub.publish(vels)

    def runLoop(self):
        self.FollowingLeft = self.readLidar(LaserScan)
        self.ChooseSide() # Can set the self.followingLeft value away from the default.
        self.wheelOutput[1] = self.TrackWall()
        self.updateVelocity() #Set values for the twist object
    
def main(args=None):
    rclpy.init(args=args)
    wally = WallFollower() # This initiates a lidar-subscribing timer
    print("Node Initiated.")
    rclpy.spin(wally)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
