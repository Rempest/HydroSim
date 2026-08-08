# HydroSim

Hydro Sim is a simple underwater world created for Gazebo Sim Harmonic, designed for testing ROVs and AUVs in underwater environments and phenomena.

The project provides a custom underwater environment with rocks, corals, sea stars, seaweed, a seabed and other environmental elements.

## Screenshots
<img width="1028" height="911" alt="Hydro_sim1" src="https://github.com/user-attachments/assets/78337da1-3255-4035-9ecb-2eb28adb981a" />
<img width="1028" height="911" alt="Hydro_sim2" src="https://github.com/user-attachments/assets/2eaa955b-afb6-4449-a1ad-c8976e0cc80f" />
<img width="1028" height="911" alt="Hydro_sim3" src="https://github.com/user-attachments/assets/444f24e8-706a-4cda-9489-dc1a33c05f18" />
<img width="1028" height="911" alt="Hydro_sim4" src="https://github.com/user-attachments/assets/fdcafbc7-b8ea-4645-8757-4c46a29e7bff" />
<img width="1028" height="911" alt="Hydro_sim5" src="https://github.com/user-attachments/assets/6670093f-19b6-4327-a0bf-4f2e23f2743c" />


## Features

- Underwater environment for Gazebo Sim Harmonic
- Large 1000 × 1000 m environment
- Custom seabed
- Rocks and coral formations
- Sea stars
- Seaweed
- Custom 3D models
- PBR materials and textures
- Gazebo SDF world
- ROS 2 integration
- Designed for future ROV and AUV simulation
- Suitable as a base environment for underwater robotics research and experimentation

## Project Structure

```text
hydro_sim/
├── CMakeLists.txt
├── launch/
│   └── launch_hydro.py
├── materials/
│   └── stone/
│       └── seamless_stone_pbr_texture_with_rugged_natural_rock_surface.png
├── models/
│   ├── corals/
│   ├── rocks/
│   ├── sand/
│   ├── seastar/
│   ├── seaweed/
│   └── shipwreck/
├── package.xml
├── screenshots/
│   ├── Hydro_sim1.png
│   ├── Hydro_sim2.png
│   ├── Hydro_sim3.png
│   ├── Hydro_sim4.png
│   └── Hydro_sim5.png
└── worlds/
    ├── generated_reef.sdf
    └── hydro.sdf
```
## Requirements
· Ubuntu 24.04
· ROS 2 Jazzy
· Gazebo Sim Harmonic
· Python 3
· ros_gz_sim

## Installation
__1. Clone the repository:__ 
```
git clone https://github.com/Rempest/HydroSim.git
cd HydroSim
```

__2. Source ROS 2 Jazzy:__
```
source /opt/ros/jazzy/setup.bash
```
__3. Build the workspace:__
```
colcon build
```
__4. Running__
```
ros2 launch hydro_sim launch_hydro.py
```
*Gazebo Sim should open and load the underwater environment.*

## World

**The simulation contains a large and simple underwater environment with a 1000 × 1000 m area.**

**The environment currently includes:**
```
*- rocky areas*
*- coral*
*- sea stars*
*- seaweed*
*- seabed*
*- underwater materials and textures*
```
**The world is built using SDF and can be extended with additional models and underwater structures.**
