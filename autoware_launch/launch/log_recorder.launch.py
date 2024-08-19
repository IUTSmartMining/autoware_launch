from datetime import datetime
import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    custom_folder = f"{os.getenv('HOME')}/rosbags/autoware_prototype/{timestamp}_recording"
    topics = [
        '/oau/sensory',
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
        '/planning/scenario_planning/trajectory',
        '/perception/object_recognition/objects',
        '/apu/actuatory',
        '/oau/sensory_raw',
    ]

    return LaunchDescription([
        ExecuteProcess(
            cmd = ['ros2', 'bag', 'record'] + topics + ['-o', custom_folder],
            output = 'screen'
        ),
    ])
