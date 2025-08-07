from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription


def generate_launch_description():

    webserver_folder = PathJoinSubstitution(
            [FindPackageShare("teleop_twist_web"), "config"])

    rosbridge_launch = IncludeLaunchDescription(
        XMLLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('rosbridge_server'),
                'launch',
                'rosbridge_websocket_launch.xml'
            ])
        ]),
    )
    webserver_node = ExecuteProcess(
        cmd=[[
            'python -m http.server 8000',
            ' -d ', webserver_folder
        ]],
        shell=True
    )

    nodes = [
        rosbridge_launch,
        webserver_node
    ]

    return LaunchDescription(nodes)

