# HydroSim

Hydro Sim is a simple underwater world created for Gazebo Sim Harmonic, designed for testing ROVs and AUVs in underwater environments and phenomena.

The project provides a custom underwater environment with rocks, corals, sea stars, seaweed, a seabed and other environmental elements.

## Screenshots

![Hydro Sim 1](screenshots/Hydro_sim1.png)

![Hydro Sim 2](screenshots/Hydro_sim2.png)

![Hydro Sim 3](screenshots/Hydro_sim3.png)

![Hydro Sim 4](screenshots/Hydro_sim4.png)

![Hydro Sim 5](screenshots/Hydro_sim5.png)

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

##Installation
__1. Clone the repository:__ 
```
git clone https://github.com/Rempest/HydroSim.git
cd HydroSim
```




