# ros2_teleop_twist_web
Basic Web Control Of a ROS2 Robot, using ROS2 Rosbridge.

This package launches ROS2 Rosbridge and also a Python http server (to serve up a Javascript program to the browser). The Javascript creates a virtual joystick to move the robot. On a touch screen drag the red dot up/down for forwards backwards anf left/right to turn.
These actions instruct Rosbridge to publish TwistStamped messages on topic /cmd_vel.

Additionally has a camera option which if set to true launches the web video server, cam2image with topic set to /web_video_server/image, and this image will be displayed live in the browser.

This is currently for touch devices only.

# Tested

teleop_twist_web: Raspberry Pi 3B+, Ubuntu 22.04, ROS2 Jazzy (RoboStack).

Browser: Safari iPAD 15.6.1 and Safari iPhone SE 18.6

# Launch

To use:

```ros2 launch teleop_twist_web teleop_twist_web_launch.py camera:=true```

on web browser:
    http://192.168.1.178:8000/

replace the above IP address with the address of the server where you launch teleop_twist_web.

# References

ROS Bridge server: https://github.com/RobotWebTools/rosbridge_suite

ROSLibJS: https://github.com/RobotWebTools/roslibjs

Aryan Jagushte, ROS2 Web Interface, YouTube. 01/12/2024. https://www.youtube.com/watch?v=Imb6kCqkCpA


Following contains useful example on how to use touch displays in a browser:
https://stackoverflow.com/questions/58337243/canvas-touch-event-js

General discussion on touch control:
https://seblee.me/2011/04/multi-touch-game-controller-in-javascripthtml5-for-ipad/
