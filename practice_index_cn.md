# 实践索引

本库只保存代码、许可证、环境说明与版本信息，**不安装依赖、不启动仿真、不运行代码、不操作机器人**。下表的“评价方法”是阅读与对照用的建议，不是本轮已经完成的复现结果。随仓库带来的小型说明性数据若已保留，见各包内文件清单；大型数据集、模型权重、仿真场景和安装包已在抓取时丢弃。

| 编号 | 任务 | 前置知识 | 软硬件条件（阅读用） | 评价方法（未执行） | 本地路径 | 许可证/版本 |
|---|---|---|---|---|---|---|
| RA02X01 | 阅读欠驱动课程 notebook 与习题结构 | 线性代数、最优控制概念、Python | Drake + Python；本轮不安装 | 对照讲义章节能否独立写出 LQR/轨迹优化步骤 | `02_robot_modeling_control/practice/MIT_Underactuated_repo_en` | 仓库 LICENSE；已有复用 |
| RA02X02 | 对照 Modern Robotics 实现正逆解与轨迹 | RA02B01 前 9 章 | Python 或 MATLAB | 抽查正运动学/Jacobian 示例与书中公式是否同构 | `02_robot_modeling_control/practice/NxRLab_ModernRobotics_code_en.tar` | 仓库 LICENSE |
| RA02X03 | 阅读 Pinocchio 官方 examples | 刚体动力学、URDF 概念 | Pinocchio（C++/Python） | 能指出正/逆动力学调用入口，不要求数值复现 | `02_robot_modeling_control/practice/pinocchio_examples_en.tar` | BSD-2-Clause |
| RA03X01 | 阅读 OpenCV 5 标定/特征/立体示例 | 相机模型、Python 或 C++ | OpenCV 5.0.0 | 能把示例映射到标定、特征、立体流程 | `03_perception/practice/opencv_5.0.0_samples_en.tar` | Apache-2.0；已有复用 |
| RA03X02 | 阅读 Open3D 点云与配准示例 | 点云、刚体变换 | Open3D / Python | 能说明 ICP/可视化脚本输入输出 | `03_perception/practice/open3d_examples_en.tar` | MIT |
| RA04X01 | 阅读 GTSAM 位姿图/IMU 小例子 | 因子图、高斯估计 | GTSAM C++ 或 Python | 能画出示例因子图，不跑优化 | `04_localization_mapping/practice/gtsam_examples_en.tar` | BSD-3-Clause |
| RA05X01 | 阅读 Freiburg 移动机器人习题 | 概率、运动模型 | Python；课程页环境 | 对照课件检查运动模型/滤波习题表述 | `05_planning_navigation/practice/Freiburg_MobileRobotics_2023SS_Exercises_en` | 课程公开材料；已有复用 |
| RA05X02 | 阅读 Nav2 启动与参数示例 | ROS 2、代价地图概念 | ROS 2 Jazzy + Nav2 | 能列出 bringup 启动文件与关键参数名 | `05_planning_navigation/practice/nav2_docs_bringup_en.tar` | Apache-2.0 |
| RA05X03 | 阅读 OMPL 采样规划 demos | 构型空间、碰撞检测概念 | OMPL / C++ | 能指出规划器类型与问题定义接口 | `05_planning_navigation/practice/ompl_demos_en.tar` | BSD-3-Clause |
| RA06X01 | 阅读操作课习题与 notebook | 刚体运动、Python、Drake 概念 | Drake；本轮不安装 | 对照 RA06C01 章节列出习题目标 | `06_manipulation/practice/MIT_Manipulation_repo_en` | 仓库 LICENSE；已有复用 |
| RA06X02 | 阅读 MoveIt 2 教程源 | ROS 2、运动规划 | MoveIt 2 + ROS 2 | 能说明规划场景与正逆解调用链 | `06_manipulation/practice/moveit2_tutorials_en.tar` | BSD-3-Clause |
| RA06X03 | 阅读 Drake 操作站/夹爪示例 | Drake 文档、Python | Drake | 能对应 Manipulation Station 组件 | `06_manipulation/practice/drake_manipulation_examples_en.tar` | BSD-3-Clause |
| RA07X01 | 阅读 LeRobot 库、配置与训练脚本结构 | Python、PyTorch、模仿/强化学习概念 | 普通 GPU 工作站（未配置）；**不含权重** | 能指出数据集接口与策略脚本，不训练 | `07_learning_embodied_ai/practice/huggingface_lerobot_src_en.tar` | Apache-2.0 |
| RA08X01 | 阅读 tf2 广播/监听示例 | ROS 2 坐标系 | ROS 2 geometry2 | 能画出父子坐标系与广播频率设定 | `08_multi_robot/practice/ros2_geometry2_tf2_examples_en.tar` | BSD |
| RA09X01 | 阅读 ROS 2 官方 examples | Linux、Python 或 C++ | ROS 2 Jazzy | 能对应节点/话题/服务/动作/参数/launch | `09_software_simulation/practice/ros2_examples_en.tar` | Apache-2.0 |
| RA09X02 | 阅读 ros2_control 硬件与控制器 demo | ROS 2、控制接口 | ros2_control | 能区分 hardware interface 与 controller | `09_software_simulation/practice/ros2_control_demos_en.tar` | Apache-2.0 |

提交号见各条目 `state/items/RA*X*.json` 的 `commit` 字段以及 `catalog_cn.csv`。

建议实践顺序（仍不执行）：RA02X02 → RA03X01 → RA04X01 → RA09X01 / RA08X01 → 再按专题选 Nav2、MoveIt、Pinocchio/Drake、LeRobot。
