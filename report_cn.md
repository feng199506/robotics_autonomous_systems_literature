# 本轮报告：机器人与自主系统资料库

检索执行日：2026-10-30。只收集整理，不安装软件、不启动仿真、不运行代码、不操作机器人、不上传 GitHub、不删除资料。**本轮结束，不进入第三类「无人机与空中机器人」。**

根目录：`/root/robotics_autonomous_systems_literature/`

## 1. 各类型成功下载数量及全库去重数

只计完整保存且核验通过的条目。

| 类型 | 已核验 | 目标 | 新下载 | 已有复用 | 失败 |
|---|---|---|---|---|---|
| 教材/专著 | **18** | 15–25 | 9 | 9 | 1 |
| 大学课程 | **13** | 10–15 | 5 | 8 | 1 |
| 论文/综述/教程 | **68** | 约 50 | 68 | 0 | 5 |
| 官方工具文档 | **13** | 8–12 | 12 | 1 | 0 |
| 实践项目 | **16** | 10–15 | 12 | 4 | 0 |

全库去重已核验 **128** 条：新下载 **106**，已有复用 **22**（来自控制/AI/编程资料库的副本，不移动原件，不把复用计为新成果）。

工具文档 13 套略高于 8–12：均为点名官方栈（ROS 2、Gazebo、MuJoCo、Isaac Lab、MoveIt 2、Nav2、Pinocchio、Drake、ros2_control、OpenCV、GTSAM、OMPL、Open3D）。实践 16 套略高于 10–15。

## 2. 论文近三年占比

- 时间窗口：arXiv v1 或等价首次公开日 2023-10-30 至 2026-10-30。
- 近三年核验 **47** 篇，作为约 50 篇的主体。
- 必要经典计入配额 6 篇：Cadena SLAM 2016、Solà micro Lie 2018、ORB-SLAM3 2020、Diffusion Policy 2023-03、Pinocchio 解析导数 RSS 2018、Nav2 Marathon 2 2020。
- 配额合计 **53** 篇，近三年占比 **88.7%**（≥85%）。
- 另有 **15** 篇三年前经典单列并写明理由，不挤占分母。

## 3. 覆盖情况

**经典基础：** Lynch/Park《Modern Robotics》、LaValle《Planning Algorithms》、Barfoot 状态估计第 2 版、Dellaert/Kaess 因子图、Boyd 凸优化、Särkkä 滤波、Blanco SE(3)、Solà 四元数 ESKF、ETH 动力学 2017 脚本、MIT 2.12 OCW、欠驱动与操作讲义、Freiburg 移动机器人、CMU 16-811、Stanford AA274A。

**现代方法：** SLAM Handbook 2026、Gaussian/NeRF SLAM 综述与系统、FAST-LIVO2、KISS-SLAM、VLA/模仿学习综述、扩散策略、Mobile ALOHA、OpenVLA、Isaac Lab/Orbit 生态、仓储 MAPF 布局。不是「只下载具身大模型论文」。

**软件（均已核验归属与版本口径）：** ROS 2 **Jazzy**（非 ROS 1）；Gazebo Harmonic 与 Jazzy 配对；MuJoCo；Isaac Lab（与 Isaac Sim 区分）；MoveIt 2；Nav2；Pinocchio；Drake；ros2_control Rolling 官方 PDF；OpenCV 5.0.0；GTSAM；OMPL；Open3D。镜像触达配额后文档数已达标，记为部分范围。

**实践：** 16 套官方示例/课程仓库，含许可证与提交号；未执行、不声称已复现。见 `practice_index_cn.md`。

应用：移动导航、机械臂操作、仓储物流论文、制造/接触操作课。未用无人机专项资料补数量。

## 4. 缺口、失败、残缺、待核实

| 条目 | 处理 |
|---|---|
| RA05B03 Correll LibreTexts | Full.pdf 仅 6 页，不计。MIT Press 2022 作者声明不可公开张贴 |
| RA04C03 Bonn MSR2 2021 | 课程页解析到 0 个 PDF |
| RA05P04 / RA07P09 / RA09P02 / RA08P04 / RA08P05 | 占位 arXiv 标题不匹配或非 OA，失败不计 |
| MLS 全书、Szeliski 2e | 出版社撤回或需填表，未抓 |
| Webots、PCL、Ceres Solver、RViz 独立包 | 未单独镜像。RViz 含于 ROS 2 文档；Ceres 站点 Anubis/超时；ros2_control 已有官方 PDF 与 demos |
| 部分 HTML 文档 | 配额截断，正文文件数已达标，范围见 catalog「范围说明」 |

没有「待核验仍计数」的条目。失败见 `download_failures_cn.csv`。

## 5. 目录路径与续跑

```text
/root/robotics_autonomous_systems_literature/
  README_cn.md  catalog_cn.csv  progress_cn.csv
  search_log_cn.md  download_failures_cn.csv
  learning_path_cn.md  tools_map_cn.md  practice_index_cn.md
  report_cn.md
  01_mathematical_foundations/ … 10_deployment_applications/
  scripts/   state/items/
```

```bash
cd /root/robotics_autonomous_systems_literature
python3 -I scripts/fetch_en.py status
python3 -I scripts/fetch_en.py run --retry-failed   # 已 ok/failed 默认跳过
python3 -I scripts/build_catalog_en.py
```

已核验与已失败默认不重下。不下载场景包、数据集、权重、安装包。

等待第三类别指令。
