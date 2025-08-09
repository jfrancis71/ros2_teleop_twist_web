# ros2_teleop_twist_web
Simple Web Control Of a ROS2 Robot, using ROS2 Rosbridge

Note this is a simple web control using push buttons to make small robot movements, forwards/backwards and left/right. It is probably too basic to be practically useful; but it does demonstrate how to get a web browser to interact with ROS2 using ROS2 Rosbridge.

This package launches ROS2 Rosbridge and also a Python http server (to serve up a Javascript program to the browser). This Javascript program instructs Rosbridge to publish TwistStamped messages on topic /cmd_vel when one of the direction buttons is pressed.

# Tested

Tested on ROS2 Jazzy.

# Launch

To use:

```ros2 launch teleop_twist_web teleop_twist_web_launch.py```

on web browser:
    http://192.168.1.178:8000/

replace the above IP address with the address of the server where you launch teleop_twist_web.

# References

ROS Bridge server: https://github.com/RobotWebTools/rosbridge_suite

ROSLibJS: https://github.com/RobotWebTools/roslibjs

Aryan Jagushte, ROS2 Web Interface, YouTube. 01/12/2024. https://www.youtube.com/watch?v=Imb6kCqkCpA



