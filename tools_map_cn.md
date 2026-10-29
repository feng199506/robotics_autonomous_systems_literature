# 官方工具图谱

记录项目归属、维护状态、版本与兼容关系。文档以检索日 2026-10-30 的公开站点为准。不安装软件。

## 中间件与应用栈（ROS 2）

| 组件 | 归属 | 本库版本选择 | 兼容说明 | 资料编号 |
|---|---|---|---|---|
| ROS 2 | Open Robotics | **Jazzy Jalisco**（LTS，2024-05 至 2029-05） | 与 Humble（LTS 至 2027-05）并存。Iron 已结束。本库不收 ROS 1 教程。 | RA09T01 |
| tf2 / geometry2 | Open Robotics（`ros2/geometry2`） | 随 ROS 2 发行版 | 坐标变换；多机/多传感器定位依赖它 | RA08X01 |
| rosbag2 | Open Robotics | Jazzy 文档中的录制/回放教程 | 数据记录与回放，不是 ROS 1 `rosbag` | RA09T01 |
| RViz 2 | Open Robotics | Jazzy 文档中的可视化条目 | 与 ROS 1 RViz 不混用 | （见 ROS 2 文档包） |
| Nav2 | Open Navigation / ros-navigation | 当前 `docs.nav2.org` | ROS 2 导航栈；对应论文 “Marathon 2”（RA09P01） | RA09T06，实践 RA05X02 |
| MoveIt 2 | PickNik / moveit | `moveit.picknik.ai/main` | **不是 MoveIt 1**。规划插件常接 OMPL | RA09T05，实践 RA06X02 |
| ros2_control | ros-controls | 官方 Rolling PDF 导出 + `ros2_control_demos` | 硬件接口与控制器；接 MoveIt/Gazebo。Jazzy 无同名 PDF，架构与 Rolling 文档共用。 | 文档 RA09T09；实践 RA09X02 |

Gazebo 与 ROS 2 发行版配对（公开文档口径）：**Harmonic ↔ Jazzy**；Ionic ↔ Kilted。本库仿真文档以 Harmonic/Jazzy 为主。

## 仿真

| 工具 | 归属 | 用途 | 资料编号 |
|---|---|---|---|
| Gazebo | Open Robotics | 刚体/传感器仿真，机器人系统集成 | RA09T02 |
| MuJoCo | Google DeepMind | 接触丰富的物理仿真，学习与控制常用 | RA09T03 |
| Isaac Sim / Isaac Lab | NVIDIA | Sim 是仿真应用，Lab 是其上的学习/任务框架。不下载安装包与资源包 | RA09T04；论文 RA09P02（Orbit，Lab 前身） |
| Drake | MIT / TRI | 模型基设计、轨迹优化、操作示例 | RA09T08，实践 RA06X03 |
| Webots | Cyberbotics | 本轮优先 Gazebo/MuJoCo/Isaac Lab；若镜像失败则记缺口 | （待核验） |

## 动力学、规划、估计、感知库

| 工具 | 归属 | 用途 | 资料编号 |
|---|---|---|---|
| Pinocchio | Inria / Stack of Tasks | 刚体算法与解析导数 | RA09T07，实践 RA02X03 |
| OMPL | Rice Kavraki Lab | 采样运动规划，常被 MoveIt 调用 | RA05T01，实践 RA05X03 |
| GTSAM | Georgia Tech / borglab | 因子图平滑与建图 | RA04T01，实践 RA04X01；教材 RA04B03 |
| Ceres Solver | Google | 通用非线性最小二乘（标定、BA） | （镜像若失败见失败表） |
| OpenCV | OpenCV team | 图像、标定、特征、DNN | RA03T01（复用编程库 5.0.0），实践 RA03X01 |
| Open3D | Intel ISL | 点云、网格、配准、重建 | RA03T02，实践 RA03X02 |
| PCL | Point Cloud Library | 点云处理；本轮优先 Open3D+PCL 文档视镜像结果 | （待核验） |

## 代表性 SLAM 实现（官方说明，不作无人机专项）

| 项目 | 说明 | 本库处理 |
|---|---|---|
| ORB-SLAM3 | 视觉/视觉惯性/多地图开源库 | 论文 RA04P02（经典） |
| GTSAM 示例 | 位姿图/IMU 小例子 | RA04X01 |
| Nav2 | 激光/代价地图导航，不是视觉 SLAM | RA09T06 |
| SLAM Handbook 2026 | 社区手册，含视觉/激光/IMU | 教材 RA04B04 |

不下载词表、数据集或大型词汇树。

## 学习栈对应

- 机械臂建模控制：Pinocchio + Drake + MoveIt 2 + ros2_control
- 移动导航：ROS 2 + Nav2 + Gazebo + tf2
- 定位建图：GTSAM + OpenCV/Open3D + Barfoot/SLAM Handbook
- 学习与操作：MuJoCo / Isaac Lab / Drake notebooks（MIT Manipulation）
