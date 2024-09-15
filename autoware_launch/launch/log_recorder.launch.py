from datetime import datetime
import os

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction, ExecuteProcess, DeclareLaunchArgument

def launch_setup(context):
    folder_name = LaunchConfiguration('folder_name')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(
        os.getenv('HOME'),
        'rosbags',
        folder_name.perform(context),
        f'{timestamp}_recording'
    )
    topics = [
        '/oau/sensory_raw',
        '/oau/sensory',
        '/oau/actuatory_raw',
        '/oau/actuatory',
        '/autoware/autopilot',
        '/autopilot/log/gps_pos',
        '/autopilot/log/apu_pos',
        '/autopilot/log/apu_speed',
        '/autopilot/log/apu_yaw',
        '/diagnostics',
        '/diagnostics_graph',
        '/control/command/control_cmd',
        '/system/fail_safe/mrm_state',
        '/system/mrm/emergency_stop/operate',
        '/system/mrm/comfortable_stop/operate',
        '/system/mrm/pull_over_manager/operate',
        '/sensing/gnss/raynmand/nav_sat_fix',
        '/sensing/gnss/pose_with_covariance',
        '/sensing/imu/imu_raw',
        '/sensing/imu/imu_data',
        '/vehicle/status/velocity_status',
        '/sensing/vehicle_velocity_converter/twist_with_covariance',
        '/localization/pose_twist_fusion_filter/pose_with_covariance',
        '/localization/twist_estimator/twist_with_covariance',
        '/localization/acceleration'
        '/planning/scenario_planning/trajectory',
        '/perception/object_recognition/objects',
        '/tf',
        '/api/fail_safe/mrm_state'
    ]

    return [ExecuteProcess(
        cmd=['ros2', 'bag', 'record'] + topics + ['-o', path],
        output='screen')]

def generate_launch_description():
    folder_name_arg = DeclareLaunchArgument(
        'folder_name',
        description='Name of the folder to store the recorded rosbag'
    )
    
    return LaunchDescription([
        folder_name_arg,
        OpaqueFunction(function=launch_setup),
    ])
