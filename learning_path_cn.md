# 学习路线

检索日 2026-10-30。路线只关联本库已核验资料的编号与本地路径。论文编号随下载进度补充；未核验条目不写入路径表。

阅读顺序：**数学与刚体运动 → 运动学和动力学 → 概率估计与感知 → 定位建图 → 规划控制 → 操作或移动机器人专题 → 学习方法 → 仿真与实际部署。**

三条专题路线共享前半段基础，后半段分叉。先修不足时回到对应教材，不要跳到具身大模型论文。

## 0. 公共基础（三条路线共用）

| 阶段 | 建议资料 | 路径 |
|---|---|---|
| 刚体、螺旋、SE(3) | RA02B01 Lynch & Park《Modern Robotics》第 1–4 章 | `02_robot_modeling_control/books/LynchPark_ModernRobotics_updated1stEd_en.pdf` |
| SE(3) 参数化 | RA01B04 Blanco 教程 | `01_mathematical_foundations/books/Blanco_SE3TransformationParameterizations_2010_en.pdf` |
| 四元数与误差状态 | RA01B05 Solà ESKF 笔记 | `01_mathematical_foundations/books/Sola_QuaternionKinematicsErrorStateKF_2017_en.pdf` |
| 李群短教程 | RA01P01 Solà micro Lie theory | `01_mathematical_foundations/papers/2018_Sola_MicroLieTheory_en.pdf` |
| 机器人数学课 | RA01C01 CMU 16-811（Erdmann，Fall 2025） | `01_mathematical_foundations/courses/CMU_16811_MathFundamentalsRobotics_Notes_en` |
| 凸优化 | RA01B01 Boyd & Vandenberghe | `01_mathematical_foundations/books/BoydVandenberghe_ConvexOptimization_2004_en.pdf` |
| 优化算法 | RA01B03 Kochenderfer《Algorithms for Optimization》 | `01_mathematical_foundations/books/Kochenderfer_AlgorithmsForOptimization_2019_en.pdf` |
| 变分与最优控制 | RA01B02 Liberzon | `01_mathematical_foundations/books/Liberzon_CalculusOfVariationsOptimalControl_2011_en.pdf` |
| 本科入门课 | RA02C02 MIT 2.12 OCW（Asada & Leonard，Fall 2005） | `02_robot_modeling_control/courses/MIT_212_2005Fall_OCWCoursePackage_en.zip` |

练习（不执行，只读代码与说明）：RA02X02 Modern Robotics 官方代码 `02_robot_modeling_control/practice/NxRLab_ModernRobotics_code_en.tar`。

---

## 1. 移动机器人与自主导航

**目标：** 会读运动模型与滤波器，能把激光/视觉前端接到估计与规划，能在概念上使用 ROS 2 + Nav2 + 仿真，不把无人机课程当作本路线材料。

1. **运动学与控制基础**  
   RA02B01 第 13 章（轮式）+ RA02B04 ETH Robot Dynamics 2017 脚本 `02_robot_modeling_control/books/ETH_RobotDynamics_HS2017_script_en.pdf`。

2. **概率与滤波**  
   RA04B02 Särkkä《Bayesian Filtering and Smoothing》`04_localization_mapping/books/Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf`  
   RA04C01 Stanford EE363（Boyd）`04_localization_mapping/courses/Stanford_EE363_2026Spring_LectureSlides_en`

3. **状态估计与 SLAM**  
   RA04B01 Barfoot 第 2 版 `04_localization_mapping/books/Barfoot_StateEstimationForRobotics_2ndEd_en.pdf`  
   RA04B03 Dellaert & Kaess 因子图 `04_localization_mapping/books/DellaertKaess_FactorGraphsRobotPerception_2017_en.pdf`  
   RA04B04 SLAM Handbook 2026 `04_localization_mapping/books/CarloneEtAl_SLAMHandbook_2026_en.pdf`  
   课程：RA04C02 Bonn Photogrammetry I&II `04_localization_mapping/courses/Bonn_Photogrammetry_2021_Slides_en`；RA03C03 UZH VAMR Fall 2025 `03_perception/courses/UZH_VAMR_2025Fall_Slides_en`  
   经典综述（单列）：RA04P01 Cadena TRO 2016；视觉惯性实现 RA04P02 ORB-SLAM3。

4. **感知前端**  
   RA03B01 Solem 计算机视觉草稿 `03_perception/books/Solem_ProgrammingComputerVisionWithPython_CCdraft_en.pdf`  
   RA03C01 Stanford CS231n 讲义；RA03C02 MIT 6.801 OCW  
   工具：RA03T01 OpenCV 文档（复用）；实践 RA03X01 / RA03X02。

5. **规划与导航课**  
   RA05B01 LaValle《Planning Algorithms》`05_planning_navigation/books/LaValle_PlanningAlgorithms_2006_en.pdf`  
   RA05B02 Kochenderfer《Algorithms for Decision Making》`05_planning_navigation/books/Kochenderfer_AlgorithmsForDecisionMaking_2022_en.pdf`  
   RA05C01 Freiburg Introduction to Mobile Robotics SS 2023 `05_planning_navigation/courses/Freiburg_MobileRobotics_2023SS_Slides_en`  
   RA05C02 Stanford AA274A/AA174A 2024–25 `05_planning_navigation/courses/Stanford_AA274A_2024_LectureNotes_en.pdf`

6. **软件栈**  
   文档：RA09T01 ROS 2 Jazzy（核验通过后）、RA09T06 Nav2、RA09T02 Gazebo Harmonic（与 Jazzy 配对）、RA05T01 OMPL。  
   实践：RA09X01 `09_software_simulation/practice/ros2_examples_en.tar`；RA08X01 tf2 `08_multi_robot/practice/ros2_geometry2_tf2_examples_en.tar`；RA05X02 Nav2 `05_planning_navigation/practice/nav2_docs_bringup_en.tar`；RA05X03 OMPL demos `05_planning_navigation/practice/ompl_demos_en.tar`；RA05X01 Freiburg 习题（复用）。  
   经典系统文：RA09P01 Nav2 Marathon 2。

7. **决策与部署**  
   RA01B03 / RA05B02 用于不确定下的决策；RA10B01 Brunton `10_deployment_applications/books/Brunton_DataDrivenScienceEngineering_en.pdf`。仓储多机见路线交叉 RA08 实践与论文。

---

## 2. 机械臂与操作

**目标：** 正逆运动学、动力学、轨迹与力/阻抗概念、规划到抓取接触，能把 MoveIt 2 / Pinocchio / Drake 对上课程，而不是从 VLA 论文倒推。

1. **建模**  
   RA02B01 第 4–8 章；RA02B04 ETH 动力学脚本；RA02C02 MIT 2.12。  
   实践：RA02X02 Modern Robotics 代码；RA02X03 Pinocchio examples `02_robot_modeling_control/practice/pinocchio_examples_en.tar`。

2. **控制与轨迹**  
   RA02B02 Rawlings MPC `02_robot_modeling_control/books/Rawlings_ModelPredictiveControl_2ndEd_en.pdf`  
   RA02B03 Murray Optimization-Based Control `02_robot_modeling_control/books/Murray_OptimizationBasedControl_en.pdf`  
   RA02C01 MIT Underactuated（Tedrake，6.8210/6.832）`02_robot_modeling_control/courses/MIT_Underactuated_Online_Notes_html_en`  
   实践：RA02X01 `02_robot_modeling_control/practice/MIT_Underactuated_repo_en`；RA09X02 ros2_control demos `09_software_simulation/practice/ros2_control_demos_en.tar`。

3. **操作主课**  
   RA06C01 MIT Robotic Manipulation（Tedrake，6.4212/6.800）`06_manipulation/courses/MIT_RoboticManipulation_Online_Notes_html_en`  
   实践：RA06X01 `06_manipulation/practice/MIT_Manipulation_repo_en`；RA06X03 Drake 操作示例 `06_manipulation/practice/drake_manipulation_examples_en.tar`。

4. **运动规划接到臂**  
   RA05B01 LaValle；工具 RA09T05 MoveIt 2、RA05T01 OMPL、RA09T08 Drake。  
   实践：RA06X02 `06_manipulation/practice/moveit2_tutorials_en.tar`。

5. **感知用于抓取**  
   RA03T01 OpenCV、RA03T02 Open3D；近三年三维视觉/抓取论文（RA03P*、RA06P*，以 catalog 已核验为准）。

6. **部署**  
   RA10B01；仿真文档 RA09T03 MuJoCo、RA09T04 Isaac Lab、RA09T08 Drake。不要下载场景包与权重。

---

## 3. 机器人学习与具身智能

**目标：** 先掌握控制与操作的模型基路径，再读模仿/强化学习与 VLA；本路线论文不得挤掉前两路线的经典教材。

1. **控制与操作前置**  
   完成路线 2 的第 1–3 步（Modern Robotics + Underactuated + Manipulation 讲义）。

2. **强化学习基础**  
   RA07B01 Sutton & Barto 第 2 版 `07_learning_embodied_ai/books/SuttonBarto_ReinforcementLearning_2ndEd_2020_en.pdf`  
   RA07C02 UCL Silver 2015 `07_learning_embodied_ai/courses/UCL_RL_Silver_2015_Slides_en`  
   RA07C01 Berkeley CS285 Spring 2026 `07_learning_embodied_ai/courses/Berkeley_CS285_2026Spring_Slides_en`

3. **视觉与表征**  
   RA03C01 CS231n；RA03B01。

4. **模仿、世界模型、VLA（近三年论文为主）**  
   以 catalog 中 `07_learning_embodied_ai/papers/` 已核验 PDF 为准。入门综述顺序建议：RA07P04 模仿学习综述 → RA07P02 机器人基础模型综述 → RA07P03 VLA 综述，然后再读单一模型论文。经典 RA07P01 Diffusion Policy 单列。

5. **实践代码（不运行、不声称复现）**  
   RA07X01 LeRobot 源码（已丢弃权重大文件）`07_learning_embodied_ai/practice/huggingface_lerobot_src_en.tar`  
   RA06X01 MIT Manipulation notebooks（配套讲义，不执行）。

6. **仿真到现实与评测**  
   RA10B01；论文目录 `10_deployment_applications/papers/` 中已核验的 Sim-to-Real / 评测基准。工具：MuJoCo、Isaac Lab、Drake 文档。

---

## 课程元数据（官方页）

| 编号 | 学校 | 课程代码 | 教师 | 学期 | 官方主页 |
|---|---|---|---|---|---|
| RA01C01 | Carnegie Mellon | 16-811 | Michael Erdmann | Fall 2025 | https://www.cs.cmu.edu/~me/811/ |
| RA02C01 | MIT | 6.8210 / 6.832 | Russ Tedrake | 持续更新讲义 | https://underactuated.csail.mit.edu/ |
| RA02C02 | MIT OCW | 2.12 | Harry Asada; John Leonard | Fall 2005 | https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/ |
| RA03C01 | Stanford | CS231n | Fei-Fei Li et al. | 当前公开讲义 | https://cs231n.github.io/ |
| RA03C02 | MIT OCW | 6.801 / 6.866 | Berthold Horn | Fall 2004 | https://ocw.mit.edu/courses/6-801-machine-vision-fall-2004/ |
| RA03C03 | UZH / ETH | VAMR | Davide Scaramuzza | Fall 2025 | https://rpg.ifi.uzh.ch/teaching.html |
| RA04C01 | Stanford | EE363 | Stephen Boyd | 课件页当前版 | https://ee363.stanford.edu/ |
| RA04C02 | University of Bonn | Photogrammetry I & II | Cyrill Stachniss | 2021/22 | https://www.ipb.uni-bonn.de/photo12-2021/ |
| RA05C01 | University of Freiburg | Introduction to Mobile Robotics | Burgard et al. | SS 2023 | http://ais.informatik.uni-freiburg.de/teaching/ss23/robotics/ |
| RA05C02 | Stanford | AA274A / AA174A | Zardini; Lorenzetti; Pavone | Autumn 2024–25 | https://stanfordasl.github.io/PoRA-I/aa174a_aut2425/ |
| RA06C01 | MIT | 6.4212 / 6.800 | Russ Tedrake | 持续更新讲义 | https://manipulation.csail.mit.edu/ |
| RA07C01 | UC Berkeley | CS285 | Sergey Levine | Spring 2026 | https://rail.eecs.berkeley.edu/deeprlcourse/ |
| RA07C02 | UCL / DeepMind | COMPM050 / COMPGI13 | David Silver | 2015 | https://www.davidsilver.uk/teaching/ |

Bonn MSR2（RA04C03）课件页未解析到 PDF，不列入路线。

---

## 使用说明

- 编号以 `catalog_cn.csv` 中“完整性=完整（已核验）”为准；本文件路径在资料补齐后与 catalog 对齐。
- 复用条目来自控制/AI/编程资料库的副本，不移动原件。
- 实践项目见 `practice_index_cn.md`：未执行，不声称已复现。
