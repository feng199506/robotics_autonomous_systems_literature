# 检索日志

检索执行日：2026-10-30。本轮只收集“机器人与自主系统”，不进入无人机专项。

## 平台与原则

- 教材/讲义：作者站点、大学课程页、MIT OCW、LibreTexts、Cambridge/MIT Press 作者公开 PDF。
- 论文：arXiv / 作者主页 / HAL。Crossref 仅作日期核验，不绕过付费墙。
- 软件：项目官方文档站点与 GitHub 官方仓库。ROS 2 与 ROS 1 分开；本轮主体为 ROS 2 Jazzy。
- 复用：核验后复制 `control_systems_automation_literature`、`ai_undergraduate_graduate_curriculum_literature`、`programming_reference_literature` 中已核验文件，不移动原件。

排除：付费墙 PDF、摘要/目录页、无人机专项课程（如 UZH Vision-Based Drone Flight 研讨课）、大型数据集/权重/安装包、MLS 全书（出版社 2020 年撤回在线 PDF）。

## 主要检索词（英文）

`modern robotics lynch park preprint`；`planning algorithms lavalle pdf`；`barfoot state estimation robotics pdf`；`factor graphs dellaert kaess pdf`；`slam handbook carlone 2026`；`tedrake manipulation notes`；`underactuated robotics`；`scaramuzza VAMR slides`；`AA274A principles of robot autonomy notes`；`16-811 math fundamentals robotics`；`stachniss photogrammetry slides`；`ROS 2 jazzy documentation`；`nav2 docs`；`moveit 2 tutorials`；`isaac lab documentation`；`pinocchio documentation`；`gtsam examples`。

论文：近三年 CoRL/RSS/ICRA/TRO/IJRR 与 arXiv cs.RO，主题覆盖 SLAM、操作、导航、VLA、仿真到现实、多机器人；故意限制 VLA 占比。

## 执行摘要

1. 建立 `robotics_autonomous_systems_literature/` 与可续跑脚本（改编自控制资料库 fetch 流水线）。
2. 复用控制/AI/编程库中与刚体、估计、优化、视觉、强化学习、OpenCV、MIT 操作/欠驱动课程相关的已核验资料。
3. 新下载 Lynch/Park 已在 AI 库；本轮新下 LaValle、Dellaert/Kaess、SLAM Handbook、Kochenderfer 两本、Sutton/Barto、Blanco SE(3)、Sola 四元数 ESKF、ETH Robot Dynamics 脚本等。
4. 课程新下 MIT 2.12 OCW、Stanford AA274A 讲义、UZH VAMR 2024/2025 课件、CMU 16-811 笔记、Bonn Photogrammetry I&II。Freiburg MSR2 2021 页面未解析到 PDF 链接，记失败。
5. 实践以官方 Git 稀疏克隆为主，丢弃大文件与权重。
6. 工具文档用 wget 有限深度镜像；完整 API 历史版本不抓。
7. 论文先按精选 arXiv 编号下载并用 PDF 标题词核验；arXiv API 与站点其他文献库共享限速，元数据核验可续跑。

## 排除记录

- Murray/Li/Sastry《A Mathematical Introduction to Robotic Manipulation》全文：MLSwiki 声明出版社 2020-01 撤回在线 PDF。
- Correll《Introduction to Autonomous Robots》MIT Press 2022：作者声明不可公开张贴编译 PDF；LibreTexts Full.pdf 仅 6 页，不计。
- Szeliski《Computer Vision》第 2 版：需填写下载表，视为访问限制，未抓。
- UZH “Vision-Based Drone Flight”研讨课：无人机专项，本轮不收。
- ETH Robot Dynamics 当前 Moodle 讲义：需选课登录；改用 2017 实验室公开脚本。

## 收尾（2026-10-30）

- 教材 18 / 课程 13 / 论文 68 / 工具 13 / 实践 16；全库去重 128。
- HAL Pinocchio 库介绍文被 Anubis 拦截，改用 RSS 2018 公开论文集 PDF（RA02P01）。
- 若干占位 arXiv 编号标题不匹配，已换成核验过的 OA 编号后重试；仍失败 5 篇计入失败表。
- ROS 2 / Gazebo / MoveIt 2 / Nav2 / Drake / GTSAM / OMPL / Open3D 镜像触达配额，文档数达标后复验通过，记部分范围。
- 近三年 47 篇 + 必要经典 6 篇为配额（53），占比 88.7%；其余经典单列。
- 未进入无人机专项收集。

