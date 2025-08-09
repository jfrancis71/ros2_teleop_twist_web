from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition


def generate_launch_description():

    camera_launch_arg = DeclareLaunchArgument(
        'camera',
        description='Launch camera node.',
        default_value='false'
    )

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
    camera_node = Node(
        package='image_tools',
        executable='cam2image',
        parameters=[{"frequency": 10.0}],
        condition=IfCondition(LaunchConfiguration('camera'))
    )
    web_video_server_node = Node(
        package='web_video_server',
        executable='web_video_server',
        condition=IfCondition(LaunchConfiguration('camera'))
    )

    nodes = [
        camera_launch_arg,
        rosbridge_launch,
        webserver_node,
        camera_node,
        web_video_server_node
    ]

    return LaunchDescription(nodes)

