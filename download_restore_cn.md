# 下载与解压恢复说明（机器人与自主系统文献库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含以下内容，不含 PDF 全文、课程讲义、工具文档镜像和实践项目：
  - 总目录 `catalog_cn.csv`、进度、学习路线、工具对照、实践索引、检索记录、失败清单和本轮报告；
  - 脚本和断点状态（`state/`）；
  - 本说明。

  仓库原有的 `main` 分支没有改动。
- **Release `robotics-full-20261029`**：2 个独立的不压缩 `.tar` 包，合起来就是完整的资料库，包括 10 个子方向目录下的全部教材、课程、论文、工具文档和实践项目。

Release 页面：https://github.com/feng199506/robotics_autonomous_systems_literature/releases/tag/robotics-full-20261029

## 1. 包列表

| 包文件名 | 内容范围（按路径顺序） |
|---|---|
| `robotics_autonomous_systems_20261029_batch001_cn_en.tar` | 顶层目录与报告、`scripts/`、`state/`、`01_mathematical_foundations/` 至 `04_localization_mapping/` 全部内容，`05_planning_navigation/` 的 books、courses 和前 4 篇论文，以及各子方向的空占位目录 |
| `robotics_autonomous_systems_20261029_batch002_cn_en.tar` | `05_planning_navigation/` 的其余 2 篇论文、practice、tools，`06_manipulation/` 至 `10_deployment_applications/` |

每个文件属于哪个包，见 `archive_index_cn.csv`。它是 UTF-8 带 BOM 编码，可直接用 Excel 打开，共 1,863 行，其中 1,849 个文件、14 个空目录。

- 每个包都可以**单独解压**，不需要拼接。
- 两个包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包没有压缩，所需磁盘空间约等于包的大小。全部解压约需 **2.8 GiB**。如果还要展开里面的文档镜像和示例包（见第 4 节），建议预留 6 GiB。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 2 个 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到**同一个下载文件夹**，例如 `D:\下载\robotics\`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断时，可以在浏览器的下载列表里点“恢复”，或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，核对每个包的大小。在文件属性窗口里看“大小”一项的字节数，不要看“占用空间”。

## 3. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\robotics\`。

1. 在下载文件夹中，按住 Ctrl 选中 2 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\robotics\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 点确定。

也可以逐个解压：每个包都右键 → WinRAR → **解压文件…**，目标路径都填同一个 `D:\robotics\`。不要用“解压到 robotics_autonomous_systems_20261029_batch00X_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

解压后的目录结构：

```
D:\robotics\
├─ README_cn.md、catalog_cn.csv、learning_path_cn.md、report_cn.md、tools_map_cn.md …
├─ 01_mathematical_foundations\ … 10_deployment_applications\
├─ scripts\
└─ state\
```

### Windows 文件名兼容

发布包里的文件名都已经处理过，在 Windows 下解压不会因为文件名报错，最长相对路径 156 个字符。资料库的本地原件没有改动。每一处改名和改写都逐条记在 `windows_rename_map_cn.csv` 里。

- **两份 MIT 网页版讲义**：
  - 涉及的讲义：
    - 《Underactuated Robotics》：`02_robot_modeling_control/courses/MIT_Underactuated_Online_Notes_html_en/`
    - 《Robotic Manipulation》：`06_manipulation/courses/MIT_RoboticManipulation_Online_Notes_html_en/`
  - 两份讲义里共有 9 个文件名带 `?`，例如 `icp_noise.html?height=240px.html`。这些 `?` 已改成 `_`。
  - 引用这些文件的 13 个网页已同步改写，离线打开时仍能正常显示。
- **6 个官方文档离线镜像**：Open3D、GTSAM、Gazebo、Isaac Lab、MoveIt 2、MuJoCo 的内层 `.tar`。
  - 这 6 个包里共有 279 个样式、脚本和字体文件的名字带 `?v=…`。
  - 这 6 个包已重新打包：文件名里的 `?` 改成 `_`，网页里的对应链接同步改写，其余内容不变。
  - 因此这 6 个文件的字节数与资料库原件不同，这是正常的。
- 其余 18 个内层 `.tar` 和 3 个 `.zip` 已逐个检查，名字里没有 Windows 不允许的字符，也没有只差大小写的文件，没有改动。

## 4. 内层归档（.zip / .tar）

资料库本身就把一部分资料整包保存。解压发布包之后，它们仍是单个文件，需要时再单独解开：

- **3 个 `.zip`**：MIT OCW 2.12 和 6.801 课程包，以及 OpenCV 5.0.0 的 HTML 文档。
- **24 个 `.tar`**：
  - 工具文档的 HTML 离线镜像，包括 ROS 2、Gazebo、MuJoCo、Isaac Lab、MoveIt 2、Nav2、Pinocchio、Drake、Open3D、GTSAM、OMPL 等；
  - 实践项目的源码或示例快照，在各子方向的 `practice/` 下。

解开方法：右键该文件 → WinRAR → **解压到 “文件名\”**。HTML 镜像解开后，用浏览器打开其中的 `index.html`。

另有 3 个实践项目以普通目录保存，不需要再解包：

- `MIT_Underactuated_repo_en`
- `MIT_Manipulation_repo_en`
- `Freiburg_MobileRobotics_2023SS_Exercises_en`

## 5. Linux / macOS

```bash
mkdir -p ~/robotics
for f in robotics_autonomous_systems_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/robotics || echo "FAILED: $f"; done
```

## 6. 资料状态说明（来自资料库自身的目录，与打包无关）

- **只计已核验条目**：全库去重共 128 条，`catalog_cn.csv` 中全部标为“完整（已核验）”。
  - 教材 18、大学课程 13、论文 68、官方工具文档 13、实践项目 16。
  - 论文中近三年 47 篇，计入配额的必要经典 6 篇，近三年占比 88.7%。
- **失败 7 项**：记录在 `download_failures_cn.csv`，不计入，也没有对应文件。其中教材 1 项、课程 1 项、论文 5 项。
- **快照时间**：本次按 2026-10-29 20:39（中欧时间）的资料库内容打包。打包前先把整个资料库复制成一份快照，打包用的就是这份快照。资料库最后一次写入是在 20:35。

## 7. 完整性说明

- 本次发布只登记了上传状态：GitHub API 显示附件为 `uploaded`，且远端大小等于本地大小。**没有**做下载回验和哈希校验。
- 资料库本身没有整库的 SHA-256 清单。
- 资料库中的资料文件都已打包，没有遗漏。只排除了以下不属于资料的内容：
  - 本地 `.git/`；
  - `scripts/__pycache__/` 中的 3 个 `.pyc`；
  - `state/` 下 10 个空的 `.lock` 锁文件。
- 参考项目里的 `poetry.lock` 是项目依赖清单，属于资料内容，已打包。
