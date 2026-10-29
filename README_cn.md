# 机器人与自主系统文献库

本目录收集“机器人与自主系统”的系统学习资料：教材、大学课程、论文、官方工具文档与实践项目。只做收集、核验与登记，不安装软件、不启动仿真、不运行代码、不操作机器人。

- 检索执行日：2026-10-30
- 论文时间窗口：首次公开日期 2023-10-30 至 2026-10-30。arXiv 取 v1 提交日。
- 计数规则：只计已完整保存且核验通过的条目。摘要、试读、残缺、仅链接、失败、待核验不计。
- 本轮不收集第三类“无人机与空中机器人”专项资料。

<!-- PROGRESS:START -->
检索执行日：2026-10-30。论文近三年窗口：2023-10-30 至 2026-10-30。只计已完整保存且核验通过的资料。

| 类型 | 已核验 | 目标 | 新下载 | 已有复用 | 失败 | 说明 |
|---|---|---|---|---|---|---|
| 教材/专著 | 18 | 15–25 | 9 | 9 | 1 | 经典教材允许旧版 |
| 大学课程 | 13 | 10–15 | 5 | 8 | 1 | 完整讲义/课件包计一次 |
| 论文/综述/教程 | 68 | 约 50 | 68 | 0 | 5 | 近三年 47；必要经典计入配额后占比 88.7%（配额 53）；其余经典单列 15 |
| 官方工具文档 | 13 | 8–12 | 12 | 1 | 0 | HTML 离线包，记录范围 |
| 实践项目 | 16 | 10–15 | 12 | 4 | 0 | 含许可证；不执行代码 |

全库去重已核验：128；其中新下载 106，已有复用 22。
<!-- PROGRESS:END -->

## 目录结构

| 路径 | 内容 |
|---|---|
| [catalog_cn.csv](catalog_cn.csv) | 全库总目录（仅已核验） |
| [progress_cn.csv](progress_cn.csv) | 按类型进度 |
| [download_failures_cn.csv](download_failures_cn.csv) | 失败、残缺、待核验（不计） |
| [search_log_cn.md](search_log_cn.md) | 检索平台、用词、排除与执行日志 |
| [learning_path_cn.md](learning_path_cn.md) | 三条学习路线及资料编号 |
| [tools_map_cn.md](tools_map_cn.md) | 官方工具归属、版本与兼容 |
| [practice_index_cn.md](practice_index_cn.md) | 实践项目任务、前置与评价方法 |
| [report_cn.md](report_cn.md) | 本轮收集结果与缺口 |
| `01_`–`10_` | 十个子方向，各含 books/courses/papers/tools/practice |
| `scripts/` | 种子、下载与核验脚本 |
| `state/items/` | 断点续跑状态 |

十个子方向：

| 编号 | 子目录 | 主题 |
|---|---|---|
| 01 | `01_mathematical_foundations` | 刚体运动、SE(3)、李群、运动学动力学与优化基础 |
| 02 | `02_robot_modeling_control` | 正逆运动学、Jacobian、轨迹跟踪、力/阻抗/操作空间控制 |
| 03 | `03_perception` | 相机、图像与点云、深度、重建、检测分割、融合 |
| 04 | `04_localization_mapping` | 概率机器人、滤波、里程计、SLAM、因子图 |
| 05 | `05_planning_navigation` | 图搜索、采样规划、轨迹优化、导航、动态环境 |
| 06 | `06_manipulation` | 机械臂、抓取、接触、灵巧与移动操作、协作 |
| 07 | `07_learning_embodied_ai` | 模仿/强化学习、VLA、世界模型、技能迁移 |
| 08 | `08_multi_robot` | 多机定位、协作感知、任务分配、分布式决策 |
| 09 | `09_software_simulation` | ROS 2、仿真器、中间件、标定、日志回放 |
| 10 | `10_deployment_applications` | 仿真到现实、辨识、实时与可靠性、应用案例 |

编号规则：`RA` + 主题两位 + 类型字母 + 序号。B 教材，C 课程，P 论文，T 工具文档，X 实践。

文件命名：自建与下载交付文件在扩展名前标注语言（`_en` / `_cn`）。上游源码与离线 HTML 内部保留原文件名，外层归档包加语言后缀。

## 核验标准

- PDF：HTTP 200，`%PDF-` 头，pypdf 可解析，页数与标题词匹配通过。
- 课程包：一套计一次；多文件须可解析。
- HTML 文档：离线包记录范围，检查正文文件数。
- Git 实践：保存源码、许可证、说明；丢弃大型权重/数据集；不执行。
- 复用：从控制/AI/编程资料库复制，不移动原文件，标注“已有复用”，不重复计为独立新成果。

## 续跑

```bash
cd /root/robotics_autonomous_systems_literature
python3 -I scripts/seed_core_en.py
python3 -I scripts/seed_papers_en.py
python3 -I scripts/fetch_en.py run                  # 全部待办
python3 -I scripts/fetch_en.py run --kind pdf       # 仅 PDF
python3 -I scripts/fetch_en.py run --kind mirror    # 仅文档镜像
python3 -I scripts/fetch_en.py run --retry-failed
python3 -I scripts/fetch_en.py status
python3 -I scripts/build_catalog_en.py
```

已核验与已失败条目默认不重下。请求限速：arXiv 间隔约 4 秒。遇到 401/402/403/404/451 立即放弃。不绕过付费墙。

不下载大型仿真场景、数据集、模型权重、软件安装包、依赖缓存或构建产物。
