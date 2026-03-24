from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    return LaunchDescription([

        # Gazebo Harmonic
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', 'iris_runway.sdf'],
            output='screen'
        ),

        # ArduPilot SITL
        ExecuteProcess(
            cmd=[
                'sim_vehicle.py',
                '-v', 'ArduCopter',
                '-f', 'gazebo-iris',
                '--model=JSON'
            ],
            output='screen'
        ),
    ])
