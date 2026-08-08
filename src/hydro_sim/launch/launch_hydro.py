from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_path = get_package_share_directory("hydro_sim")
    world_path = os.path.join(
        package_path,
        "worlds",
        "hydro.sdf"
    )

    models_path = os.path.join(
        package_path,
        "models"
    )

    materials_path = os.path.join(
        package_path,
        "materials"
    )

    resource_path = ":".join([
        package_path,
        models_path,
        materials_path,
    ])

    return LaunchDescription([
        SetEnvironmentVariable(
            name="GZ_SIM_RESOURCE_PATH",
            value=resource_path
        ),

        ExecuteProcess(
            cmd=[
                "gz",
                "sim",
                "-r",
                world_path
            ],
            output="screen"
        ),
    ])