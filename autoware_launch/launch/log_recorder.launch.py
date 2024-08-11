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
    ]

    return LaunchDescription([
        ExecuteProcess(
            cmd = ['ros2', 'bag', 'record'] + topics + ['-o', custom_folder],
            output = 'screen'
        ),
    ])
