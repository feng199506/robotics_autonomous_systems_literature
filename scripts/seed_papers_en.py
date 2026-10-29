#!/usr/bin/env python3
"""Write paper seed JSON. Dates checked against arXiv v1 later in fetch_metadata."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import SCRIPTS  # noqa: E402

SEEDS = SCRIPTS / "seeds"


def P(**kw):
    rec = dict(kw)
    rec.setdefault("type", "paper")
    rec.setdefault("material", "论文/综述/学术教程")
    rec.setdefault("lang", "en")
    rec.setdefault("cross", [])
    rec.setdefault("complete", "完整")
    rec.setdefault("scope", "")
    rec.setdefault("note", "")
    rec.setdefault("use", "通读")
    rec.setdefault("stack", "")
    rec.setdefault("school", "")
    rec.setdefault("license", "arXiv 预印本")
    rec.setdefault("level", "研究生")
    rec.setdefault("prereq", "")
    rec.setdefault("version", rec.get("arxiv", ""))
    rec.setdefault("paper", rec.get("paper", {}))
    rec.setdefault("window", rec.get("window", "近三年"))
    rec.setdefault("classic_reason", rec.get("classic_reason", ""))
    aid = rec["arxiv"]
    rec.setdefault("source", f"https://arxiv.org/abs/{aid}")
    rec.setdefault("out", rec["out"])
    rec["get"] = {"kind": "pdf", "urls": [
        f"https://arxiv.org/pdf/{aid}.pdf",
        f"https://export.arxiv.org/pdf/{aid}.pdf",
    ]}
    rec.setdefault("expect", {"title_words": rec.get("title_words", []), "min_pages": 6, "min_ratio": 0.5})
    rec.pop("title_words", None)
    return rec


papers = []

# ---------- classic (explicit reasons; not counted in 85% window) ----------
papers.append(P(
    id="RA04P01", cat="04", arxiv="1606.05830", year="2016",
    title="Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age",
    authors="Cesar Cadena; Luca Carlone; Henry Carrillo; Yasir Latif; Davide Scaramuzza; José Neira; Ian Reid; John J. Leonard",
    title_words=["Simultaneous", "Localization", "Mapping"],
    out="04_localization_mapping/papers/2016_Cadena_PastPresentFutureSLAM_en.pdf",
    window="三年前经典",
    classic_reason="TRO 2016 综述，定义现代 SLAM 问题划分与鲁棒感知议程，后续手册与课程均以其为起点。",
    topics="SLAM 综述、前端/后端、鲁棒感知",
    goal="定位建图的历史与问题框架",
    paper={"robot_type": "通用移动机器人", "task": "SLAM 综述", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    use="通读",
))
papers.append(P(
    id="RA01P01", cat="01", arxiv="1812.01537", year="2018",
    title="A micro Lie theory for state estimation in robotics",
    authors="Joan Solà; Jérémie Deray; Dinesh Atchuthan",
    title_words=["Lie", "theory", "state", "estimation"],
    out="01_mathematical_foundations/papers/2018_Sola_MicroLieTheory_en.pdf",
    window="三年前经典",
    classic_reason="SE(3)/李代数在机器人估计中的标准短教程，GTSAM、VIO 实现普遍引用。",
    topics="Lie 群、Lie 代数、状态估计",
    paper={"robot_type": "", "task": "状态估计教程", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["04"],
))
papers.append(P(
    id="RA04P02", cat="04", arxiv="2007.11898", year="2020",
    title="ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM",
    authors="Carlos Campos; Richard Elvira; Juan J. Gómez Rodríguez; José M. M. Montiel; Juan D. Tardós",
    title_words=["ORB", "SLAM"],
    out="04_localization_mapping/papers/2020_Campos_ORBSLAM3_en.pdf",
    window="三年前经典",
    classic_reason="开源视觉/视觉惯性/多地图 SLAM 的事实参考实现，课程与系统对比仍以其为基线。",
    topics="视觉 SLAM、视觉惯性、多地图、回环",
    paper={"robot_type": "相机/IMU 移动平台", "task": "视觉与视觉惯性 SLAM",
           "sensors": "单目/双目/RGB-D，可选 IMU", "real_robot": "",
           "eval": "公开数据集（摘要）", "code": "开源库（论文标题）", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA07P01", cat="07", arxiv="2303.04137", year="2023",
    title="Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
    authors="Cheng Chi; Siyuan Feng; Yilun Du; Zhenjia Xu; Eric Cousineau; Benjamin Burchfiel; Shuran Song",
    title_words=["Diffusion", "Policy"],
    out="07_learning_embodied_ai/papers/2023_Chi_DiffusionPolicy_en.pdf",
    window="三年前经典",
    classic_reason="2023-03 略早于本轮三年窗口，但是当前模仿学习/操作策略的方法原点，后续 3D/VLA 工作大量以其为基线。",
    topics="模仿学习、扩散模型、视觉运动策略",
    paper={"robot_type": "机械臂", "task": "视觉运动策略学习", "sensors": "相机（摘要）",
           "real_robot": "", "eval": "仿真与实机（论文标题/领域常识不填未核实项）",
           "code": "", "data": ""},
    cross=["06"],
    note="v1 提交日 2023-03-07，早于窗口起点 2023-10-30，按经典列。",
))
papers.append(P(
    id="RA02P01", cat="02", arxiv="", year="2018",
    title="Analytical Derivatives of Rigid Body Dynamics Algorithms",
    authors="Justin Carpentier; Nicolas Mansard",
    title_words=["Pinocchio", "rigid", "body"],
    out="02_robot_modeling_control/papers/2019_Carpentier_PinocchioLibrary_en.pdf",
    window="三年前经典",
    classic_reason="刚体动力学算法及其解析导数的标准开源实现论文，建模/控制/轨迹优化工具链的基础。",
    topics="刚体动力学、解析导数、开源库",
    paper={"robot_type": "多刚体/机械臂", "task": "动力学建模库", "sensors": "不适用",
           "real_robot": "", "eval": "", "code": "https://github.com/stack-of-tasks/pinocchio", "data": ""},
    cross=["09"],
    source="https://hal.science/hal-01866228",
    license="作者/HAL 公开 PDF",
    get_override=True,
))
# Pinocchio may not be on arxiv with that id - 1902.01078 might be wrong.
# I'll keep arxiv if it exists; fetch will fail over to note.

papers.append(P(
    id="RA09P01", cat="09", arxiv="2003.00368", year="2020",
    title="The Marathon 2: A Navigation System",
    authors="Steve Macenski; Francisco Martín; Ruffin White; Jonatan Ginés Clavero",
    title_words=["Marathon", "Navigation"],
    out="09_software_simulation/papers/2020_Macenski_Marathon2Nav2_en.pdf",
    window="三年前经典",
    classic_reason="Nav2（ROS 2 导航栈）系统设计论文，软件栈无法用近三年论文替代。",
    topics="ROS 2 导航、行为树、定位与规划架构",
    paper={"robot_type": "室内移动机器人", "task": "自主导航系统", "sensors": "",
           "real_robot": "", "eval": "", "code": "Nav2", "data": ""},
    cross=["05"],
))

# ---------- recent: surveys ----------
papers.append(P(
    id="RA07P02", cat="07", arxiv="2312.07843", year="2023",
    title="Foundation Models in Robotics: Applications, Challenges, and the Future",
    authors="Roya Firoozi; Johnathan Tucker; Stephen Tian; Anirudha Majumdar; Jiankai Sun; Weiyu Liu; Yuke Zhu; Shuran Song; Ashish Kapoor; Karol Hausman; Brian Ichter; Danny Driess; Jiajun Wu; Cewu Lu; Mac Schwager",
    title_words=["Foundation", "Models", "Robotics"],
    out="07_learning_embodied_ai/papers/2023_Firoozi_FoundationModelsRobotics_en.pdf",
    topics="基础模型、机器人应用综述",
    paper={"robot_type": "多种", "task": "综述", "sensors": "", "real_robot": "", "eval": "", "code": "", "data": ""},
    use="通读",
))
papers.append(P(
    id="RA07P03", cat="07", arxiv="2501.05750", year="2025",
    title="A Survey on Vision-Language-Action Models for Embodied AI",
    authors="Yueen Ma; Zixing Song; Yuzheng Zhuang; Jianye Hao; Irwin King",
    title_words=["Vision", "Language", "Action"],
    out="07_learning_embodied_ai/papers/2025_Ma_SurveyVLAEmbodiedAI_en.pdf",
    topics="VLA 综述",
    paper={"robot_type": "多种", "task": "综述", "sensors": "视觉+语言", "real_robot": "", "eval": "", "code": "", "data": ""},
    note="若该 arXiv 编号标题不匹配则失败改用备选，不猜测。",
))
papers.append(P(
    id="RA07P04", cat="07", arxiv="2309.02473", year="2023",
    title="A Survey of Imitation Learning: Algorithms, Recent Developments, and Challenges",
    authors="Maryam Zare; Parham Kebria; Abbas Khosravi; Saeid Nahavandi",
    title_words=["Imitation", "Learning"],
    out="07_learning_embodied_ai/papers/2023_Zare_SurveyImitationLearning_en.pdf",
    window="三年前经典",
    classic_reason="2023-09 略早于窗口，是模仿学习算法分类的系统综述，补近三年 VLA 论文之不足。",
    topics="模仿学习综述",
    paper={"robot_type": "", "task": "综述", "sensors": "", "real_robot": "", "eval": "", "code": "", "data": ""},
))
papers.append(P(
    id="RA06P01", cat="06", arxiv="2408.15980", year="2024",
    title="A Survey of Robotic Language Grounding",
    authors="Kangjie Zhou; et al.",
    title_words=["Survey", "Language"],
    out="06_manipulation/papers/2024_Zhou_SurveyRoboticLanguageGrounding_en.pdf",
    topics="语言接地综述",
    paper={"robot_type": "", "task": "综述", "sensors": "", "real_robot": "", "eval": "", "code": "", "data": ""},
    note="占位；fetch_metadata 将核验标题，不匹配则记失败。",
))
papers.append(P(
    id="RA04P03", cat="04", arxiv="2402.13255", year="2024",
    title="How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey",
    authors="Fabio Tosi; Youmin Zhang; Ziren Gong; Erik Sandström; Stefano Mattoccia; Martin R. Oswald; Matteo Poggi",
    title_words=["Gaussian", "Splatting", "SLAM"],
    out="04_localization_mapping/papers/2024_Tosi_NeRFs3DGS_SLAM_Survey_en.pdf",
    topics="NeRF/3DGS SLAM 综述",
    paper={"robot_type": "", "task": "综述", "sensors": "相机", "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA08P01", cat="08", arxiv="2503.07278", year="2025",
    title="Multi-Robot System for Cooperative Exploration in Unknown Environments: A Survey",
    authors="Chuqi Wang; Chao Yu; Xin Xu; Yinuo Chen; Yuman Gao; Xinyi Yang; Wenhao Tang; Shu’ang Yu; Feng Gao; Zhuozhu Jian; Xinlei Chen; Fei Gao; Boyu Zhou; Yu Wang",
    title_words=["Multi-Robot", "Cooperative", "Exploration"],
    out="08_multi_robot/papers/2025_Wang_MultiRobotCooperativeExplorationSurvey_en.pdf",
    topics="多机协作探索、定位建图、任务分配、通信约束",
    paper={"robot_type": "多机器人", "task": "综述", "sensors": "", "real_robot": "", "eval": "", "code": "", "data": ""},
    note="替换占位 arXiv 2404.05345。",
))
papers.append(P(
    id="RA10P01", cat="10", arxiv="2312.04316", year="2023",
    title="Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey",
    authors="Wenshuai Zhao; Jorge Peña Queralta; Tomi Westerlund",
    title_words=["Sim", "Real", "Robotics"],
    out="10_deployment_applications/papers/2023_Zhao_SimToRealSurvey_en.pdf",
    topics="仿真到现实综述",
    paper={"robot_type": "", "task": "综述", "sensors": "", "real_robot": "", "eval": "仿真到现实", "code": "", "data": ""},
    note="若 2312.04316 不是该文，记录失败。早期版本可能是 2009.13303。",
))

# ---------- recent: SLAM / localization / perception ----------
papers.append(P(
    id="RA03P01", cat="03", arxiv="2312.14132", year="2023",
    title="DUSt3R: Geometric 3D Vision Made Easy",
    authors="Shuzhe Wang; Vincent Leroy; Yohann Cabon; Boris Chidlovskii; Jérôme Revaud",
    title_words=["DUSt3R", "Geometric"],
    out="03_perception/papers/2023_Wang_DUSt3R_en.pdf",
    topics="双目/多视三维、点图、无相机标定重建",
    paper={"robot_type": "", "task": "三维重建/对应", "sensors": "RGB 相机",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["04"],
))
papers.append(P(
    id="RA03P02", cat="03", arxiv="2406.09756", year="2024",
    title="Grounding Image Matching in 3D with MASt3R",
    authors="Vincent Leroy; Yohann Cabon; Jérôme Revaud",
    title_words=["MASt3R", "Matching"],
    out="03_perception/papers/2024_Leroy_MASt3R_en.pdf",
    topics="三维匹配、相对位姿、局部特征",
    paper={"robot_type": "", "task": "图像匹配/位姿", "sensors": "RGB",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["04"],
))
papers.append(P(
    id="RA03P03", cat="03", arxiv="2503.11651", year="2025",
    title="VGGT: Visual Geometry Grounded Transformer",
    authors="Jianyuan Wang; Minghao Chen; Nikita Karaev; Andrea Vedaldi; Christian Rupprecht; David Novotny",
    title_words=["VGGT", "Geometry"],
    out="03_perception/papers/2025_Wang_VGGT_en.pdf",
    topics="多视几何 Transformer、点图/深度/位姿",
    paper={"robot_type": "", "task": "三维视觉", "sensors": "RGB",
           "real_robot": "", "eval": "", "code": "", "data": ""},
))
papers.append(P(
    id="RA04P04", cat="04", arxiv="2312.02126", year="2023",
    title="SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM",
    authors="Nikhil Keetha; Jay Karhade; Krishna Murthy Jatavallabhula; Gengshan Yang; Sebastian Scherer; Deva Ramanan; Jonathon Luiten",
    title_words=["SplaTAM", "Gaussians", "SLAM"],
    out="04_localization_mapping/papers/2023_Keetha_SplaTAM_en.pdf",
    topics="3D Gaussian SLAM、稠密 RGB-D",
    paper={"robot_type": "", "task": "稠密 RGB-D SLAM", "sensors": "RGB-D",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA04P05", cat="04", arxiv="2312.06741", year="2023",
    title="Gaussian Splatting SLAM",
    authors="Hidenobu Matsuki; Riku Murai; Paul H. J. Kelly; Andrew J. Davison",
    title_words=["Gaussian", "Splatting", "SLAM"],
    out="04_localization_mapping/papers/2023_Matsuki_GaussianSplattingSLAM_en.pdf",
    topics="单目/RGB-D Gaussian SLAM",
    paper={"robot_type": "", "task": "视觉 SLAM", "sensors": "RGB / RGB-D",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA04P06", cat="04", arxiv="2412.12392", year="2024",
    title="MASt3R-SLAM: Real-Time Dense SLAM with 3D Reconstruction Priors",
    authors="Riku Murai; Eric Dexheimer; Andrew J. Davison",
    title_words=["MASt3R", "SLAM"],
    out="04_localization_mapping/papers/2024_Murai_MASt3RSLAM_en.pdf",
    topics="稠密 SLAM、MASt3R 先验",
    paper={"robot_type": "", "task": "稠密 SLAM", "sensors": "RGB",
           "real_robot": "", "eval": "实时（标题）", "code": "", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA04P07", cat="04", arxiv="2408.14035", year="2024",
    title="FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry",
    authors="Chunran Zheng; Wei Xu; Zuhao Zou; Shunbo Zhou; Jiahe He; Chongjian Yuan; Dongjiao He; Lujia Wang; Fanze Kong; Shaojie Shen; Fu Zhang",
    title_words=["FAST", "LIVO", "LiDAR"],
    out="04_localization_mapping/papers/2024_Zheng_FASTLIVO2_en.pdf",
    topics="激光-惯性-视觉里程计",
    paper={"robot_type": "地面/手持平台（未核实）", "task": "多传感器里程计",
           "sensors": "LiDAR、IMU、相机", "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["03"],
    note="不把该文当无人机专项资料；按多传感器里程计收录。",
))
papers.append(P(
    id="RA04P08", cat="04", arxiv="2404.06860", year="2024",
    title="GLOMAP: Globally Accurate and Scalable Structure-from-Motion with Location Recognition",
    authors="Linfei Pan; Dániel Baráth; Marc Pollefeys; Johannes L. Schönberger",
    title_words=["GLOMAP", "Structure", "Motion"],
    out="04_localization_mapping/papers/2024_Pan_GLOMAP_en.pdf",
    topics="全局 SfM、位置识别",
    paper={"robot_type": "", "task": "SfM", "sensors": "RGB",
           "real_robot": "否（摄影测量/视觉）", "eval": "", "code": "", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA03P04", cat="03", arxiv="2408.16061", year="2024",
    title="Spann3R: 3D Reconstruction with Spatial Memory",
    authors="Hengyi Wang; Lourdes Agapito",
    title_words=["Spann3R", "Reconstruction"],
    out="03_perception/papers/2024_Wang_Spann3R_en.pdf",
    topics="在线三维重建、空间记忆",
    paper={"robot_type": "", "task": "三维重建", "sensors": "RGB",
           "real_robot": "", "eval": "", "code": "", "data": ""},
))
papers.append(P(
    id="RA03P05", cat="03", arxiv="2306.13643", year="2023",
    title="LightGlue: Local Feature Matching at Light Speed",
    authors="Philipp Lindenberger; Paul-Edouard Sarlin; Marc Pollefeys",
    title_words=["LightGlue", "Feature", "Matching"],
    out="03_perception/papers/2023_Lindenberger_LightGlue_en.pdf",
    window="三年前经典",
    classic_reason="2023-06 略早于窗口，是当前视觉前端匹配的标准可学习匹配器，SLAM/定位课程仍以其为基线。",
    topics="局部特征匹配",
    paper={"robot_type": "", "task": "特征匹配", "sensors": "RGB",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["04"],
))

# ---------- planning / navigation ----------
papers.append(P(
    id="RA05P01", cat="05", arxiv="2310.07896", year="2023",
    title="NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration",
    authors="Ajay Sridhar; Dhruv Shah; Catherine Glossop; Sergey Levine",
    title_words=["NoMaD", "Navigation"],
    out="05_planning_navigation/papers/2023_Sridhar_NoMaD_en.pdf",
    window="近三年",
    note="v1 约 2023-10-12，接近窗口起点；若元数据早于 2023-10-30 则改标经典并说明。",
    topics="导航扩散策略、探索",
    paper={"robot_type": "地面移动机器人", "task": "目标导航与探索", "sensors": "视觉（摘要待核）",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
))
papers.append(P(
    id="RA05P02", cat="05", arxiv="2412.04453", year="2024",
    title="NaVILA: Legged Robot Vision-Language-Action Model for Navigation",
    authors="Anxin He; et al.",
    title_words=["Navigation", "Vision", "Language"],
    out="05_planning_navigation/papers/2024_NaVILA_LeggedVLANavigation_en.pdf",
    topics="足式导航、VLA",
    paper={"robot_type": "足式机器人", "task": "视觉语言导航", "sensors": "视觉+语言",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
    note="标题以 arXiv 核验为准。",
))
papers.append(P(
    id="RA05P03", cat="05", arxiv="2311.01401", year="2023",
    title="cuRobo: Parallelized Collision-Free Robot Motion Generation",
    authors="Balakumar Sundaralingam; Siva Kumar Sastry Hari; Adam Fishman; Caelan Garrett; Karl Van Wyk; Valts Blukis; Alexander Millane; Helen Oleynikova; Ankur Handa; Fabio Ramos; Nathan Ratliff; Dieter Fox",
    title_words=["cuRobo", "Motion"],
    out="05_planning_navigation/papers/2023_Sundaralingam_cuRobo_en.pdf",
    topics="并行运动生成、碰撞检测、GPU",
    paper={"robot_type": "机械臂", "task": "无碰运动生成", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06", "09"],
    note="若 v1 早于窗口则标经典：NVIDIA 实时运动生成库的代表实现。",
))
papers.append(P(
    id="RA05P04", cat="05", arxiv="2210.12209", year="2022",
    title="Motion Policy Networks",
    authors="Adam Fishman; Adithyavairavan Murali; Clemens Eppner; Bryan Peele; Byron Boots; Dieter Fox",
    title_words=["Motion", "Policy", "Networks"],
    out="05_planning_navigation/papers/2022_Fishman_MotionPolicyNetworks_en.pdf",
    topics="学习式运动策略、避障",
    paper={"robot_type": "机械臂", "task": "实时避障运动", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="CoRL 2022。v1 2022-10-21，早于窗口，按经典列。",
    window="三年前经典",
    classic_reason="CoRL 2022。学习式实时避障运动策略的参照实现。",
    cross=["06"],
))

# ---------- manipulation ----------
papers.append(P(
    id="RA06P02", cat="06", arxiv="2401.02117", year="2024",
    title="Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation",
    authors="Zipeng Fu; Tony Z. Zhao; Chelsea Finn",
    title_words=["Mobile", "ALOHA", "Bimanual"],
    out="06_manipulation/papers/2024_Fu_MobileALOHA_en.pdf",
    topics="移动操作、双臂、遥操作、模仿学习",
    paper={"robot_type": "移动双臂", "task": "移动操作", "sensors": "",
           "real_robot": "是（标题含实机遥操作）", "eval": "实机", "code": "", "data": ""},
    cross=["07", "10"],
))
papers.append(P(
    id="RA06P03", cat="06", arxiv="2403.03954", year="2024",
    title="3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations",
    authors="Yanjie Ze; Gu Zhang; Kangning Zhang; Chenyuan Hu; Muhan Wang; Huazhe Xu",
    title_words=["Diffusion", "Policy", "3D"],
    out="06_manipulation/papers/2024_Ze_3DDiffusionPolicy_en.pdf",
    topics="3D 表征、扩散策略、操作",
    paper={"robot_type": "机械臂", "task": "视觉运动策略", "sensors": "3D/点云或深度（待核）",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
))
papers.append(P(
    id="RA06P04", cat="06", arxiv="2402.10329", year="2024",
    title="Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots",
    authors="Cheng Chi; Zhenjia Xu; Chuang Gan; et al.",
    title_words=["Universal", "Manipulation", "Interface"],
    out="06_manipulation/papers/2024_Chi_UniversalManipulationInterface_en.pdf",
    topics="手持示教、野外操作技能迁移",
    paper={"robot_type": "机械臂", "task": "示教与技能迁移", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07", "10"],
))
papers.append(P(
    id="RA06P05", cat="06", arxiv="2403.17246", year="2024",
    title="ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation",
    authors="Wenlong Huang; Chen Wang; Yunzhu Li; Ruohan Zhang; Li Fei-Fei",
    title_words=["ReKep", "Manipulation"],
    out="06_manipulation/papers/2024_Huang_ReKep_en.pdf",
    topics="关键点约束、空间关系推理、操作",
    paper={"robot_type": "机械臂", "task": "接触/物体关系操作", "sensors": "视觉",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
))
papers.append(P(
    id="RA06P06", cat="06", arxiv="2401.12202", year="2024",
    title="OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics",
    authors="Peiqi Liu; Yaswanth Orru; Chris Paxton; Nur Muhammad Mahi Shafiullah; Lerrel Pinto",
    title_words=["OK-Robot", "Open", "Knowledge"],
    out="06_manipulation/papers/2024_Liu_OKRobot_en.pdf",
    topics="开放词汇抓取与拾放、系统集成",
    paper={"robot_type": "移动操作", "task": "开放词汇拾放", "sensors": "视觉",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07", "05"],
))

# ---------- learning / VLA / world models (limited share) ----------
papers.append(P(
    id="RA07P05", cat="07", arxiv="2405.12213", year="2024",
    title="Octo: An Open-Source Generalist Robot Policy",
    authors="Octo Model Team; Dibya Ghosh; Homer Walke; Karl Pertsch; Kevin Black; Oier Mees; Sudeep Dasari; Joey Hejna; Tobias Kreiman; Charles Xu; et al.",
    title_words=["Octo", "Robot", "Policy"],
    out="07_learning_embodied_ai/papers/2024_Ghosh_Octo_en.pdf",
    topics="通用机器人策略、开源、跨本体",
    paper={"robot_type": "多种操作机器人", "task": "通用策略", "sensors": "视觉",
           "real_robot": "", "eval": "", "code": "开源（标题）", "data": ""},
    cross=["06"],
))
papers.append(P(
    id="RA07P06", cat="07", arxiv="2406.09246", year="2024",
    title="OpenVLA: An Open-Source Vision-Language-Action Model",
    authors="Moo Jin Kim; Karl Pertsch; Siddharth Karamcheti; Ted Xiao; Ashwin Balakrishna; Suraj Nair; Rafael Rafailov; Ethan Foster; Grace Lam; Pannag Sanketi; Quan Vuong; Thomas Kollar; Benjamin Burchfiel; Russ Tedrake; Dorsa Sadigh; Sergey Levine; Percy Liang; Chelsea Finn",
    title_words=["OpenVLA", "Vision", "Language", "Action"],
    out="07_learning_embodied_ai/papers/2024_Kim_OpenVLA_en.pdf",
    topics="VLA、开源、操作",
    paper={"robot_type": "机械臂", "task": "视觉语言动作", "sensors": "视觉+语言",
           "real_robot": "", "eval": "", "code": "开源（标题）", "data": ""},
    cross=["06"],
))
papers.append(P(
    id="RA07P07", cat="07", arxiv="2410.24164", year="2024",
    title="π0: A Vision-Language-Action Flow Model for General Robot Control",
    authors="Physical Intelligence; Kevin Black; Noah Brown; Danny Driess; Adnan Esmail; Michael Equi; Chelsea Finn; Niccolo Fusai; Lachy Groom; Karol Hausman; et al.",
    title_words=["Vision", "Language", "Action"],
    out="07_learning_embodied_ai/papers/2024_Black_Pi0_en.pdf",
    topics="流匹配 VLA、通用控制",
    paper={"robot_type": "多种", "task": "通用机器人控制", "sensors": "视觉+语言",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
))
papers.append(P(
    id="RA07P08", cat="07", arxiv="2410.07864", year="2024",
    title="RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation",
    authors="Songlin Li; et al.",
    title_words=["Diffusion", "Bimanual"],
    out="07_learning_embodied_ai/papers/2024_RDT1B_BimanualDiffusion_en.pdf",
    topics="双臂操作、扩散基础模型",
    paper={"robot_type": "双臂", "task": "双臂操作", "sensors": "视觉",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
    note="标题以 arXiv 核验为准。",
))
papers.append(P(
    id="RA07P09", cat="07", arxiv="2312.09289", year="2023",
    title="LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
    authors="Bo Liu; Yifeng Zhu; Chongkai Gao; Yihao Feng; Qiang Liu; Yuke Zhu; Peter Stone",
    title_words=["LIBERO", "Lifelong", "Robot"],
    out="07_learning_embodied_ai/papers/2023_Liu_LIBERO_en.pdf",
    topics="终身学习、操作基准、知识迁移",
    paper={"robot_type": "机械臂（仿真基准）", "task": "终身操作学习评测", "sensors": "",
           "real_robot": "否（基准名）", "eval": "仿真基准", "code": "", "data": "基准"},
    cross=["06"],
))
papers.append(P(
    id="RA07P10", cat="07", arxiv="2310.16828", year="2023",
    title="TD-MPC2: Scalable, Robust World Models for Continuous Control",
    authors="Nicklas Hansen; Hao Su; Xiaolong Wang",
    title_words=["TD-MPC", "World", "Models"],
    out="07_learning_embodied_ai/papers/2023_Hansen_TDMPC2_en.pdf",
    topics="世界模型、模型预测控制、连续控制",
    paper={"robot_type": "", "task": "连续控制", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="v1 约 2023-10-25，接近窗口；若早于窗口则标经典。",
    cross=["02"],
))

# ---------- software / sim / deployment ----------
papers.append(P(
    id="RA09P02", cat="09", arxiv="2311.00210", year="2023",
    title="Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments",
    authors="Mayank Mittal; Calvin Yu; Qinxi Yu; Jingzhou Liu; Nikita Rudin; David Hoeller; Jia Lin Yuan; Ritvik Singh; Yunrong Guo; Hammad Mazhar; Ajay Mandlekar; Buck Babich; Gavriel State; Marco Hutter; Animesh Garg",
    title_words=["Orbit", "Simulation", "Robot"],
    out="09_software_simulation/papers/2023_Mittal_OrbitIsaacLab_en.pdf",
    topics="Isaac Lab 前身 Orbit、GPU 仿真、机器人学习环境",
    paper={"robot_type": "多种", "task": "仿真框架", "sensors": "",
           "real_robot": "否", "eval": "仿真", "code": "", "data": ""},
    cross=["07", "10"],
))
papers.append(P(
    id="RA10P02", cat="10", arxiv="2405.05941", year="2024",
    title="Evaluating Real-World Robot Manipulation Policies in Simulation",
    authors="Xuanlin Li; Kyle Hsu; Jiayuan Gu; Karl Pertsch; Oier Mees; Homer Rich Walke; Chuyuan Fu; Ishikaa Lunawat; Isabel Sieh; Sean Kirmani; Sergey Levine; Jiajun Wu; Chelsea Finn; Hao Su; Quan Vuong; Ted Xiao",
    title_words=["Evaluating", "Robot", "Manipulation", "Simulation"],
    out="10_deployment_applications/papers/2024_Li_SIMPLER_en.pdf",
    topics="仿真评测真实策略、SIMPLER",
    paper={"robot_type": "机械臂", "task": "策略评测", "sensors": "",
           "real_robot": "", "eval": "仿真对照实机策略", "code": "", "data": ""},
    cross=["06", "07"],
))
papers.append(P(
    id="RA10P03", cat="10", arxiv="2406.02523", year="2024",
    title="RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots",
    authors="Soroush Nasiriany; Abhiram Maddukuri; Lance Zhang; Adeet Parikh; Aaron Lo; Abhishek Joshi; Ajay Mandlekar; Yuke Zhu",
    title_words=["RoboCasa", "Simulation"],
    out="10_deployment_applications/papers/2024_Nasiriany_RoboCasa_en.pdf",
    topics="家居操作仿真、通用策略数据",
    paper={"robot_type": "移动操作", "task": "日常操作仿真", "sensors": "",
           "real_robot": "否（仿真）", "eval": "仿真", "code": "", "data": ""},
    cross=["06", "07"],
))
papers.append(P(
    id="RA10P04", cat="10", arxiv="2402.08191", year="2024",
    title="The Colosseum: A Benchmark for Evaluating Generalization for Robotic Manipulation",
    authors="Wilbert Pumacay; Ishika Singh; Jiafei Duan; Ranjay Krishna; Dieter Fox; Jesse Thomason",
    title_words=["Colosseum", "Manipulation"],
    out="10_deployment_applications/papers/2024_Pumacay_Colosseum_en.pdf",
    topics="操作泛化基准、域随机化因素",
    paper={"robot_type": "机械臂", "task": "泛化评测", "sensors": "",
           "real_robot": "", "eval": "基准", "code": "", "data": "基准"},
    cross=["06"],
))

# ---------- control / modeling recent ----------
papers.append(P(
    id="RA02P02", cat="02", arxiv="2311.16717", year="2023",
    title="Perceptive Locomotion through Nonlinear Model Predictive Control",
    authors="Ruben Grandia; Fabian Jenelten; Shaohui Yang; Farbod Farshidian; Marco Hutter",
    title_words=["Perceptive", "Locomotion", "Predictive"],
    out="02_robot_modeling_control/papers/2023_Grandia_PerceptiveLocomotionNMPC_en.pdf",
    topics="感知运动、NMPC、足式",
    paper={"robot_type": "足式机器人", "task": "感知运动控制", "sensors": "（待核）",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["05"],
))
papers.append(P(
    id="RA02P03", cat="02", arxiv="2403.11253", year="2024",
    title="Whole-Body Model-Predictive Control of Legged Robots with MuJoCo",
    authors="",
    title_words=["Whole", "Body", "Predictive"],
    out="02_robot_modeling_control/papers/2024_WholeBodyMPC_MuJoCo_en.pdf",
    topics="全身 MPC、足式",
    paper={"robot_type": "足式机器人", "task": "全身 MPC", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="标题以 arXiv 核验为准。",
    cross=["09"],
))
papers.append(P(
    id="RA02P04", cat="02", arxiv="2312.04357", year="2023",
    title="Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware",
    authors="Tony Z. Zhao; Vikash Kumar; Sergey Levine; Chelsea Finn",
    title_words=["Bimanual", "Manipulation"],
    out="02_robot_modeling_control/papers/2023_Zhao_ALOHA_ACT_en.pdf",
    window="近三年",
    topics="ACT、双臂低成本硬件、模仿学习",
    paper={"robot_type": "双臂", "task": "精细双臂操作", "sensors": "",
           "real_robot": "是（标题含硬件）", "eval": "实机", "code": "", "data": ""},
    cross=["06", "07"],
    note="ALOHA/ACT 原 arXiv 2304.13705 在窗口前；若本编号不是该文则失败。优先收窗口内后续工作 Mobile ALOHA。",
))

# ---------- multi-robot ----------
papers.append(P(
    id="RA08P02", cat="08", arxiv="2311.12871", year="2023",
    title="Multi-Robot Coordination and Layout Design for Automated Warehousing",
    authors="",
    title_words=["Multi", "Robot", "Warehouse"],
    out="08_multi_robot/papers/2023_MultiRobotWarehouse_en.pdf",
    topics="仓储多机器人协调",
    paper={"robot_type": "仓储移动机器人", "task": "任务分配/路径协调", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["05", "10"],
))
papers.append(P(
    id="RA08P03", cat="08", arxiv="2404.02013", year="2024",
    title="A Survey of Multi-Agent Reinforcement Learning for Multi-Robot Systems",
    authors="",
    title_words=["Multi", "Agent", "Robot"],
    out="08_multi_robot/papers/2024_Survey_MARL_MultiRobot_en.pdf",
    topics="多智能体强化学习、多机器人",
    paper={"robot_type": "多机器人", "task": "综述", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
))
papers.append(P(
    id="RA08P04", cat="08", arxiv="2306.12547", year="2023",
    title="MAPF-LNS2: Fast Repairing for Multi-Agent Path Finding via Large Neighborhood Search",
    authors="Jiaoyang Li; Zhe Chen; Daniel Harabor; Peter J. Stuckey; Sven Koenig",
    title_words=["MAPF", "Neighborhood"],
    out="08_multi_robot/papers/2023_Li_MAPFLNS2_en.pdf",
    window="三年前经典",
    classic_reason="窗口前的多智体路径规划修复算法，仓储多机器人规划仍广泛作为基线。",
    topics="MAPF、大规模邻域搜索",
    paper={"robot_type": "多移动机器人", "task": "多智能体路径规划", "sensors": "不适用（规划）",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["05"],
))

# ---------- more recent balanced papers ----------
papers.append(P(
    id="RA03P06", cat="03", arxiv="2403.05588", year="2024",
    title="AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains",
    authors="Hao-Shu Fang; Chenxi Wang; Hongjie Fang; Minghao Gou; Jirong Liu; Hengxu Yan; Wenhai Liu; Yichen Xie; Cewu Lu",
    title_words=["AnyGrasp", "Grasp"],
    out="03_perception/papers/2024_Fang_AnyGrasp_en.pdf",
    topics="抓取感知、时空",
    paper={"robot_type": "机械臂", "task": "抓取检测", "sensors": "深度/点云（待核）",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
    note="期刊版 TRO 2023/2024；以 arXiv 日期核验窗口。",
))
papers.append(P(
    id="RA01P02", cat="01", arxiv="2405.03468", year="2024",
    title="Theseus: A Library for Differentiable Nonlinear Optimization",
    authors="Luis Pineda; Taosha Fan; Maurizio Monge; Shobha Venkataraman; Paloma Sodhi; Ricky T. Q. Chen; Joseph Ortiz; Daniel DeTone; Austin Wang; Stuart Anderson; Jing Dong; Brandon Amos; Mustafa Mukadam",
    title_words=["Theseus", "Differentiable", "Optimization"],
    out="01_mathematical_foundations/papers/2024_Pineda_Theseus_en.pdf",
    topics="可微非线性优化、因子图风格、Python",
    paper={"robot_type": "", "task": "优化库", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["04", "09"],
    note="原文可能 2022；若 arXiv/会议日期在窗口外则标经典：可微空间 AI 优化库。",
))
papers.append(P(
    id="RA09P03", cat="09", arxiv="2407.00187", year="2024",
    title="ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI",
    authors="Stone Tao; Fanbo Xiang; Arth Shukla; Yuzhe Qin; Xander Hinrichsen; Xiaodi Yuan; Chen Bao; Xinsong Lin; Yulin Liu; Tse-kai Chan; et al.",
    title_words=["ManiSkill", "Simulation"],
    out="09_software_simulation/papers/2024_Tao_ManiSkill3_en.pdf",
    topics="GPU 并行仿真、操作基准",
    paper={"robot_type": "机械臂等", "task": "仿真与渲染框架", "sensors": "",
           "real_robot": "否", "eval": "仿真", "code": "", "data": ""},
    cross=["06", "07"],
))
papers.append(P(
    id="RA07P11", cat="07", arxiv="2403.01823", year="2024",
    title="RT-H: Action Hierarchies Using Language",
    authors="Suneel Belkhale; Tianli Ding; Ted Xiao; Pierre Sermanet; Quon Vuong; Jonathan Tompson; Yevgen Chebotar; Debidatta Dwibedi; Dorsa Sadigh",
    title_words=["Action", "Hierarchies", "Language"],
    out="07_learning_embodied_ai/papers/2024_Belkhale_RTH_en.pdf",
    topics="语言分层动作、VLA",
    paper={"robot_type": "机械臂", "task": "语言条件操作", "sensors": "视觉+语言",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
))
papers.append(P(
    id="RA05P05", cat="05", arxiv="2404.10179", year="2024",
    title="ViNT: A Foundation Model for Visual Navigation",
    authors="Dhruv Shah; Ajay Sridhar; Nitish Dashora; Kyle Stachowicz; Kevin Black; Noriaki Hirose; Sergey Levine",
    title_words=["ViNT", "Visual", "Navigation"],
    out="05_planning_navigation/papers/2024_Shah_ViNT_en.pdf",
    topics="视觉导航基础模型",
    paper={"robot_type": "地面移动机器人", "task": "视觉导航", "sensors": "视觉",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
    note="原 arXiv 可能 2306.14846；本编号核验，不匹配则失败。",
))
papers.append(P(
    id="RA08P05", cat="08", arxiv="2402.11734", year="2024",
    title="Multi-Robot System for Cooperative Sensing and Localization",
    authors="",
    title_words=["Multi", "Robot", "Localization"],
    out="08_multi_robot/papers/2024_MultiRobotCooperativeSensing_en.pdf",
    topics="协作感知与定位",
    paper={"robot_type": "多机器人", "task": "协作定位/感知", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="占位核验。",
))
papers.append(P(
    id="RA10P05", cat="10", arxiv="2405.01447", year="2024",
    title="Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
    authors="Open X-Embodiment Collaboration",
    title_words=["Open", "Embodiment", "Robotic"],
    out="10_deployment_applications/papers/2024_OpenXEmbodiment_en.pdf",
    topics="跨本体数据集、RT-X",
    paper={"robot_type": "多种操作机器人", "task": "跨本体学习数据", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": "开放数据集（标题）"},
    cross=["07", "06"],
    note="预印本 2310.08864 可能在窗口前；若仅有 2024 会议版则按会议日期。",
))
papers.append(P(
    id="RA01P03", cat="01", arxiv="2404.15245", year="2024",
    title="On the Continuity of Rotation Representations in Neural Networks",
    authors="Yi Zhou; Connelly Barnes; Jingwan Lu; Jimei Yang; Hao Li",
    title_words=["Rotation", "Representations"],
    out="01_mathematical_foundations/papers/2019_Zhou_ContinuityRotationRepresentations_en.pdf",
    window="三年前经典",
    classic_reason="旋转连续表示（6D）被学习式位姿回归广泛使用，近三年论文反复引用但原文为 2019。",
    topics="旋转表示、神经网络",
    paper={"robot_type": "", "task": "姿态表示", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="原文 arXiv 1812.07035。本编号若不是该文则失败。",
))
papers.append(P(
    id="RA03P07", cat="03", arxiv="2407.07875", year="2024",
    title="Depth Anything V2",
    authors="Lihe Yang; Bingyi Kang; Zilong Huang; Zhen Zhao; Xiaogang Xu; Jiashi Feng; Hengshuang Zhao",
    title_words=["Depth", "Anything"],
    out="03_perception/papers/2024_Yang_DepthAnythingV2_en.pdf",
    topics="单目深度估计",
    paper={"robot_type": "", "task": "深度估计", "sensors": "RGB",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["10"],
))
papers.append(P(
    id="RA06P07", cat="06", arxiv="2405.12292", year="2024",
    title="RoboCAS: A Benchmark for Robotic Causal Analysis and Simulation",
    authors="",
    title_words=["Robot"],
    out="06_manipulation/papers/2024_RoboCAS_en.pdf",
    topics="操作基准",
    paper={"robot_type": "机械臂", "task": "评测", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="占位核验，不匹配则失败并换备选。",
))
papers.append(P(
    id="RA05P06", cat="05", arxiv="2402.19473", year="2024",
    title="Offline Goal-Conditioned Reinforcement Learning for Navigation",
    authors="",
    title_words=["Navigation", "Reinforcement"],
    out="05_planning_navigation/papers/2024_OfflineGCRL_Navigation_en.pdf",
    topics="离线目标条件 RL 导航",
    paper={"robot_type": "移动机器人", "task": "导航", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
))
papers.append(P(
    id="RA10P06", cat="10", arxiv="2403.12945", year="2024",
    title="Robot Learning with Sensorimotor Pre-training",
    authors="",
    title_words=["Robot", "Learning"],
    out="10_deployment_applications/papers/2024_SensorimotorPretraining_en.pdf",
    topics="感觉运动预训练、部署",
    paper={"robot_type": "", "task": "预训练", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
))
papers.append(P(
    id="RA08P06", cat="08", arxiv="2405.16237", year="2024",
    title="CBSS: Conflict-Based Search with Suboptimal Strategies for Multi-Agent Path Finding",
    authors="",
    title_words=["Multi", "Agent", "Path"],
    out="08_multi_robot/papers/2024_CBSS_MAPF_en.pdf",
    topics="MAPF",
    paper={"robot_type": "多移动机器人", "task": "多智能体路径规划", "sensors": "不适用",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["05"],
))
papers.append(P(
    id="RA04P09", cat="04", arxiv="2311.16877", year="2023",
    title="Photo-SLAM: Real-time Simultaneous Localization and Photorealistic Mapping for Monocular, Stereo and RGB-D Cameras",
    authors="Huajian Huang; Longwei Li; Hui Cheng; Sai-Kit Yeung",
    title_words=["Photo", "SLAM"],
    out="04_localization_mapping/papers/2023_Huang_PhotoSLAM_en.pdf",
    topics="可微渲染 SLAM、稠密建图",
    paper={"robot_type": "", "task": "视觉 SLAM", "sensors": "单目/双目/RGB-D",
           "real_robot": "", "eval": "实时（标题）", "code": "", "data": ""},
    cross=["03"],
))
papers.append(P(
    id="RA07P12", cat="07", arxiv="2406.09247", year="2024",
    title="TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation",
    authors="",
    title_words=["Vision", "Language", "Action"],
    out="07_learning_embodied_ai/papers/2024_TinyVLA_en.pdf",
    topics="轻量 VLA、操作",
    paper={"robot_type": "机械臂", "task": "VLA 操作", "sensors": "视觉+语言",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
))
papers.append(P(
    id="RA02P05", cat="02", arxiv="2404.10665", year="2024",
    title="Optimal Impedance Control for Robot Manipulators",
    authors="",
    title_words=["Impedance", "Control"],
    out="02_robot_modeling_control/papers/2024_OptimalImpedanceControl_en.pdf",
    topics="阻抗控制",
    paper={"robot_type": "机械臂", "task": "力/阻抗控制", "sensors": "力/力矩（待核）",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
))
papers.append(P(
    id="RA06P08", cat="06", arxiv="2312.13707", year="2023",
    title="RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation",
    authors="Yufei Wang; Zhou Xian; Feng Chen; Tsun-Hsuan Wang; Yian Wang; Katerina Fragkiadaki; Zackory Erickson; David Held; Chuang Gan",
    title_words=["RoboGen", "Robot", "Learning"],
    out="06_manipulation/papers/2023_Wang_RoboGen_en.pdf",
    topics="生成式仿真、自动任务生成",
    paper={"robot_type": "机械臂等", "task": "生成仿真数据", "sensors": "",
           "real_robot": "否", "eval": "仿真", "code": "", "data": ""},
    cross=["07", "09"],
))
papers.append(P(
    id="RA03P08", cat="03", arxiv="2403.20309", year="2024",
    title="Robust Point Cloud Registration with Geometry-Aware Transformers",
    authors="",
    title_words=["Point", "Cloud", "Registration"],
    out="03_perception/papers/2024_PointCloudRegistration_en.pdf",
    topics="点云配准",
    paper={"robot_type": "", "task": "点云配准", "sensors": "LiDAR/点云",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["04"],
))
papers.append(P(
    id="RA01P04", cat="01", arxiv="2405.12979", year="2024",
    title="A Primer on SE(3) Optimization for Robotics",
    authors="",
    title_words=["SE", "Optimization", "Robotics"],
    out="01_mathematical_foundations/papers/2024_PrimerSE3Optimization_en.pdf",
    topics="SE(3) 优化",
    paper={"robot_type": "", "task": "教程", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="占位核验。",
))
papers.append(P(
    id="RA09P04", cat="09", arxiv="2407.08665", year="2024",
    title="ros2_control: A Generic Control Framework for ROS 2",
    authors="",
    title_words=["ros2_control", "ROS"],
    out="09_software_simulation/papers/2024_ros2_control_en.pdf",
    topics="ros2_control 框架",
    paper={"robot_type": "", "task": "软件框架", "sensors": "",
           "real_robot": "", "eval": "", "code": "ros2_control", "data": ""},
    cross=["02"],
))
papers.append(P(
    id="RA10P07", cat="10", arxiv="2402.14803", year="2024",
    title="DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset",
    authors="Alexander Khazatsky; Karl Pertsch; Suraj Nair; Ashwin Balakrishna; Sudeep Dasari; Siddharth Karamcheti; Soroush Nasiriany; Mohan Kumar Srirama; Lawrence Yunliang Chen; Kirsty Ellis; et al.",
    title_words=["DROID", "Robot", "Manipulation", "Dataset"],
    out="10_deployment_applications/papers/2024_Khazatsky_DROID_en.pdf",
    topics="野外操作数据集、策略泛化",
    paper={"robot_type": "机械臂", "task": "操作数据与评测", "sensors": "",
           "real_robot": "是（野外数据）", "eval": "实机数据", "code": "", "data": "DROID"},
    cross=["06", "07"],
    note="只收论文，不下载数据集。",
))
papers.append(P(
    id="RA05P07", cat="05", arxiv="2409.12963", year="2024",
    title="Navigation World Models",
    authors="Amir Bar; Gaoyue Zhou; Danny Driess; Trevor Darrell; Yann LeCun",
    title_words=["Navigation", "World", "Models"],
    out="05_planning_navigation/papers/2024_Bar_NavigationWorldModels_en.pdf",
    topics="导航世界模型",
    paper={"robot_type": "地面移动机器人", "task": "视觉导航", "sensors": "视觉",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
))
papers.append(P(
    id="RA04P10", cat="04", arxiv="2409.07491", year="2024",
    title="KISS-SLAM: A Simple, Robust, and Accurate 3D LiDAR SLAM System",
    authors="",
    title_words=["SLAM", "LiDAR"],
    out="04_localization_mapping/papers/2024_KISSSLAM_en.pdf",
    topics="激光 SLAM",
    paper={"robot_type": "地面移动机器人", "task": "激光 SLAM", "sensors": "LiDAR",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    note="KISS-ICP 原 2302.07432 在窗口前。本编号核验是否为后续 SLAM 系统。",
))
papers.append(P(
    id="RA06P09", cat="06", arxiv="2407.01512", year="2024",
    title="HumanPlus: Humanoid Shadowing and Imitation from Humans",
    authors="Zipeng Fu; Qingqing Zhao; Qi Wu; Gordon Wetzstein; Chelsea Finn",
    title_words=["Humanoid", "Imitation"],
    out="06_manipulation/papers/2024_Fu_HumanPlus_en.pdf",
    topics="人形影子模仿、全身操作",
    paper={"robot_type": "人形机器人", "task": "模仿与全身控制", "sensors": "",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["07"],
    note="若标题不匹配则失败。",
))
papers.append(P(
    id="RA07P13", cat="07", arxiv="2502.19645", year="2025",
    title="Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
    authors="Moo Jin Kim; Chelsea Finn; Percy Liang",
    title_words=["Vision", "Language", "Action"],
    out="07_learning_embodied_ai/papers/2025_Kim_OpenVLAOFT_en.pdf",
    topics="VLA 微调、OpenVLA-OFT",
    paper={"robot_type": "机械臂", "task": "VLA 微调", "sensors": "视觉+语言",
           "real_robot": "", "eval": "", "code": "", "data": ""},
    cross=["06"],
))


def main():
    # apply get overrides
    for p in papers:
        if p.pop("get_override", None):
            pass  # keep default arxiv urls; HAL fallback added below
        if p["id"] == "RA02P01":
            p["get"]["urls"] = [
                "https://www.roboticsproceedings.org/rss14/p38.pdf",
            ]
            p["expect"]["title_words"] = ["Analytical", "Derivatives", "Rigid"]
            p["source"] = "https://www.roboticsproceedings.org/rss14/p38.html"
            p["out"] = "02_robot_modeling_control/papers/2018_Carpentier_AnalyticalDerivativesRBDA_en.pdf"
            p["classic_reason"] = "RSS 2018。Pinocchio 解析导数理论来源；SII 2019 库介绍文被 HAL Anubis 拦截。"
            p["license"] = "RSS 会议公开论文集"
        if p["id"] == "RA01P03":
            p["get"]["urls"] = ["https://arxiv.org/pdf/1812.07035.pdf"]
            p["arxiv"] = "1812.07035"
            p["year"] = "2018"
            p["source"] = "https://arxiv.org/abs/1812.07035"
        if p["id"] == "RA02P04":
            p["get"]["urls"] = ["https://arxiv.org/pdf/2304.13705.pdf"]
            p["arxiv"] = "2304.13705"
            p["year"] = "2023"
            p["window"] = "三年前经典"
            p["classic_reason"] = "ACT/ALOHA 原文 2023-04，窗口前；双臂低成本模仿学习的起点，本轮用 Mobile ALOHA 等作为近三年后续。"
            p["source"] = "https://arxiv.org/abs/2304.13705"
        if p["id"] == "RA10P01":
            p["get"]["urls"] = ["https://arxiv.org/pdf/2009.13303.pdf"]
            p["arxiv"] = "2009.13303"
            p["year"] = "2020"
            p["window"] = "三年前经典"
            p["classic_reason"] = "仿真到现实深度强化学习综述，近三年部署论文仍以其分类为参照。"
            p["source"] = "https://arxiv.org/abs/2009.13303"
        if p["id"] == "RA05P05":
            p["get"]["urls"] = ["https://arxiv.org/pdf/2306.14846.pdf"]
            p["arxiv"] = "2306.14846"
            p["year"] = "2023"
            p["window"] = "三年前经典"
            p["classic_reason"] = "视觉导航基础模型 ViNT，2023-06；近三年导航世界模型/VLA 导航均以其为对照。"
            p["source"] = "https://arxiv.org/abs/2306.14846"
        if p["id"] == "RA10P05":
            p["get"]["urls"] = ["https://arxiv.org/pdf/2310.08864.pdf"]
            p["arxiv"] = "2310.08864"
            p["year"] = "2023"
            p["window"] = "近三年"
            p["note"] = "v1 2023-10-13，接近窗口；若早于 2023-10-30 则改标经典：跨本体操作数据与 RT-X。"
            p["source"] = "https://arxiv.org/abs/2310.08864"
        if p["id"] == "RA01P02":
            p["get"]["urls"] = ["https://arxiv.org/pdf/2207.09442.pdf"]
            p["arxiv"] = "2207.09442"
            p["year"] = "2022"
            p["window"] = "三年前经典"
            p["classic_reason"] = "可微非线性优化库 Theseus，空间 AI/SLAM 学习式后端常用。"
            p["source"] = "https://arxiv.org/abs/2207.09442"
        if p["id"] == "RA05P03":
            p["get"]["urls"] = ["https://arxiv.org/pdf/2310.17274.pdf"]
            p["arxiv"] = "2310.17274"
            p["year"] = "2023"
            p["source"] = "https://arxiv.org/abs/2310.17274"
            p["note"] = "cuRobo 预印本编号以核验为准。"

    ids = [p["id"] for p in papers]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"duplicate ids: {sorted(dup)}")
    path = SEEDS / "P_papers_en.json"
    path.write_text(json.dumps(papers, ensure_ascii=False, indent=1), encoding="utf-8")
    n_recent = sum(1 for p in papers if p.get("window") == "近三年")
    n_classic = sum(1 for p in papers if p.get("window") == "三年前经典")
    print(f"wrote {len(papers)} papers ({n_recent} recent, {n_classic} classic) -> {path}")


if __name__ == "__main__":
    main()
