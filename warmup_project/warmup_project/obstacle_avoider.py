#Use Ranges
#move forward (0) until too close to obstacle

# get lidar scan -- if ranges[0] is < distance_threshold: stop, turn 45 degrees left, check ranges[0] again, if < distance_threshold, turn 45 degrees right (from original heading), check ranges[0]
# if < distance_threshold, repeat process in intervals of 15/30/45 degrees until the way is clear, then drive forward with new bearing for some time
# reorient to odom 0, check for obstacle at ranges[0] again