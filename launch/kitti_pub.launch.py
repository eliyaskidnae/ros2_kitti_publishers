 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    rviz_path = os.path.join(get_package_share_directory(
        'ros2_kitti_publisher'), 'rviz', 'kitti_viz.rviz')
    
    rviz = Node (
        package = 'rviz2',
        executable = 'rviz2',
        name = 'rviz2',
        output = 'screen',
        arguments = ['-d', rviz_path],
    )
    kitti_publisher = Node(package='ros2_kitti_publishers',
                            executable='kitti_publishers',
                            name='kitti_publisher_node',
                            output='screen')
        
    
    return LaunchDescription([
        robot_navigator,
        # waypoint_manager
    ])