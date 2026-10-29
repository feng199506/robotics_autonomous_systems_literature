#!/usr/bin/env python3
"""Write seed JSON for books, courses, tools, and practice (no papers)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import AI, CSA, PRG, SCRIPTS  # noqa: E402

SEEDS = SCRIPTS / "seeds"


def reuse(path, source):
    return {"kind": "reuse"}, {"path": path, "source": source}


def item(**kw):
    rec = dict(kw)
    rec.setdefault("lang", "en")
    rec.setdefault("cross", [])
    rec.setdefault("complete", "完整")
    rec.setdefault("scope", "")
    rec.setdefault("note", "")
    rec.setdefault("use", "通读")
    rec.setdefault("stack", "")
    rec.setdefault("school", rec.get("authors", ""))
    rec.setdefault("expect", {})
    rec.setdefault("paper", {})
    rec.setdefault("code", rec.get("code", ""))
    rec.setdefault("prereq", rec.get("prereq", ""))
    rec.setdefault("license", rec.get("license", ""))
    rec.setdefault("version", rec.get("version", rec.get("year", "")))
    rec.setdefault("level", rec.get("level", ""))
    rec.setdefault("topics", rec.get("topics", ""))
    rec.setdefault("goal", rec.get("goal", ""))
    rec.setdefault("origin", rec.get("source", ""))
    return rec


books, courses, tools, practice = [], [], [], []

# =====================================================================
# BOOKS
# =====================================================================
g, r = reuse(f"{AI}/books/Lynch_ModernRobotics_2017_en.pdf",
             "https://hades.mech.northwestern.edu/index.php/Modern_Robotics")
books.append(item(
    id="RA02B01", cat="02", type="book", material="教材/参考书",
    title="Modern Robotics: Mechanics, Planning, and Control (updated first edition preprint)",
    authors="Kevin M. Lynch; Frank C. Park", school="Northwestern University / Seoul National University",
    year="2019", version="updated first edition preprint, 2019-12-30 (Cambridge 2017)",
    level="本科高年级/研究生", prereq="线性代数、刚体力学、基础编程",
    topics="刚体运动、螺旋理论、正逆运动学、Jacobian、动力学、轨迹生成、运动规划、机械臂控制",
    source="https://hades.mech.northwestern.edu/index.php/Modern_Robotics",
    license="作者/Cambridge 公开预印本（个人使用）",
    goal="本科到研究生的机器人力学、规划与控制主教材",
    order=1, out="02_robot_modeling_control/books/LynchPark_ModernRobotics_updated1stEd_en.pdf",
    get=g, reuse=r, cross=["01", "05", "06"],
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    expect={"title_words": ["Modern", "Robotics", "Mechanics"], "min_pages": 400},
    use="通读",
))

g, r = reuse(f"{AI}/books/Barfoot_StateEstimationForRobotics_2ndEd_en.pdf",
             "https://asrl.utias.utoronto.ca/~tdb/")
books.append(item(
    id="RA04B01", cat="04", type="book", material="教材/参考书",
    title="State Estimation for Robotics (Second Edition)",
    authors="Timothy D. Barfoot", school="University of Toronto",
    year="2024", version="Second Edition draft compiled 2026-09-02（作者站点）",
    level="研究生", prereq="概率、线性代数、刚体运动",
    topics="Bayes 滤波、Kalman/UKF/粒子滤波、李群姿态、批量估计、位姿图、BA、SLAM",
    source="https://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser24.pdf",
    license="作者公开教学草稿；正式版 Cambridge 2024",
    goal="机器人状态估计与三维姿态的系统教材",
    order=1, out="04_localization_mapping/books/Barfoot_StateEstimationForRobotics_2ndEd_en.pdf",
    get=g, reuse=r, cross=["01", "03"],
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    expect={"title_words": ["State", "Estimation", "Robotics"], "min_pages": 400},
))

g, r = reuse(f"{CSA}/05_advanced_control/books/BoydVandenberghe_ConvexOptimization_2004_en.pdf",
             "https://web.stanford.edu/~boyd/cvxbook/")
books.append(item(
    id="RA01B01", cat="01", type="book", material="教材/参考书",
    title="Convex Optimization",
    authors="Stephen Boyd; Lieven Vandenberghe", school="Stanford University / UCLA",
    year="2004", version="Cambridge 2004（作者公开 PDF）",
    level="本科高年级/研究生", prereq="线性代数、多元微积分",
    topics="凸集、凸函数、对偶、QP/SOCP/SDP、内点法",
    source="https://web.stanford.edu/~boyd/cvxbook/",
    license="作者/Cambridge 公开教学 PDF",
    goal="轨迹优化、MPC、标定与估计中的凸优化基础",
    order=1, out="01_mathematical_foundations/books/BoydVandenberghe_ConvexOptimization_2004_en.pdf",
    get=g, reuse=r, cross=["05"],
    note="已有复用：control_systems_automation_literature",
    expect={"title_words": ["Convex", "Optimization"], "min_pages": 400},
    use="按需查阅",
))

g, r = reuse(f"{CSA}/04_estimation_identification/books/Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf",
             "https://users.aalto.fi/~ssarkka/")
books.append(item(
    id="RA04B02", cat="04", type="book", material="教材/参考书",
    title="Bayesian Filtering and Smoothing (2nd ed.)",
    authors="Simo Särkkä; Lennart Svensson", school="Aalto University / Chalmers",
    year="2023", version="Second edition（作者公开 PDF）",
    level="研究生", prereq="概率、线性系统",
    topics="Bayes 滤波、Kalman、EKF/UKF、粒子滤波、平滑",
    source="https://users.aalto.fi/~ssarkka/pub/bfs_book.html",
    license="作者/Cambridge 公开教学 PDF",
    goal="定位与传感器融合所需的贝叶斯滤波教材",
    order=2, out="04_localization_mapping/books/Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf",
    get=g, reuse=r,
    note="已有复用：control_systems_automation_literature",
    expect={"title_words": ["Bayesian", "Filtering", "Smoothing"], "min_pages": 300},
))

g, r = reuse(f"{CSA}/05_advanced_control/books/Liberzon_CalculusOfVariationsOptimalControl_2011_en.pdf",
             "https://liberzon.csl.illinois.edu/")
books.append(item(
    id="RA01B02", cat="01", type="book", material="教材/参考书",
    title="Calculus of Variations and Optimal Control Theory: A Concise Introduction",
    authors="Daniel Liberzon", school="University of Illinois Urbana-Champaign",
    year="2012", version="Princeton 2012（作者公开 PDF，封面署 2011 讲义）",
    level="研究生", prereq="常微分方程、线性代数",
    topics="变分法、Pontryagin 极小值原理、LQR、约束最优控制",
    source="https://liberzon.csl.illinois.edu/teaching/cvoc.pdf",
    license="作者公开教学 PDF",
    goal="轨迹优化与最优控制的数学基础",
    order=2, out="01_mathematical_foundations/books/Liberzon_CalculusOfVariationsOptimalControl_2011_en.pdf",
    get=g, reuse=r, cross=["02", "05"],
    note="已有复用：control_systems_automation_literature",
    expect={"title_words": ["Calculus", "Variations", "Optimal"], "min_pages": 200},
    use="按需查阅",
))

g, r = reuse(f"{CSA}/05_advanced_control/books/Rawlings_ModelPredictiveControl_2ndEd_en.pdf",
             "https://sites.engineering.ucsb.edu/~jbraw/mpc/")
books.append(item(
    id="RA02B02", cat="02", type="book", material="教材/参考书",
    title="Model Predictive Control: Theory, Computation, and Design (2nd ed.)",
    authors="James B. Rawlings; David Q. Mayne; Moritz M. Diehl",
    school="UCSB / Imperial College / University of Freiburg",
    year="2020", version="2nd edition（作者公开 PDF）",
    level="研究生", prereq="状态空间、优化",
    topics="MPC 稳定性、跟踪、经济 MPC、数值求解",
    source="https://sites.engineering.ucsb.edu/~jbraw/mpc/",
    license="作者公开教学 PDF",
    goal="机器人轨迹跟踪与约束控制常用的 MPC 教材",
    order=2, out="02_robot_modeling_control/books/Rawlings_ModelPredictiveControl_2ndEd_en.pdf",
    get=g, reuse=r, cross=["05"],
    note="已有复用：control_systems_automation_literature",
    expect={"title_words": ["Model", "Predictive", "Control"], "min_pages": 400},
    use="按需查阅",
))

g, r = reuse(f"{CSA}/05_advanced_control/books/Murray_OptimizationBasedControl_en.pdf",
             "https://www.cds.caltech.edu/~murray/")
books.append(item(
    id="RA02B03", cat="02", type="book", material="教材/参考书",
    title="Optimization-Based Control",
    authors="Richard M. Murray", school="California Institute of Technology",
    year="2010", version="作者讲义 PDF",
    level="研究生", prereq="经典/现代控制、优化",
    topics="LQR、MPC、轨迹生成、Kalman、传感器融合",
    source="https://www.cds.caltech.edu/~murray/books/AM08/pdf/obc-complete_01Jan10.pdf",
    license="作者公开教学 PDF",
    goal="把最优控制接到机器人轨迹跟踪",
    order=3, out="02_robot_modeling_control/books/Murray_OptimizationBasedControl_en.pdf",
    get=g, reuse=r, cross=["01", "05"],
    note="已有复用：control_systems_automation_literature",
    expect={"title_words": ["Optimization", "Control"], "min_pages": 100},
    use="按需查阅",
))

g, r = reuse(f"{AI}/books/Solem_ProgrammingComputerVisionWithPython_CCdraft_en.pdf",
             "http://programmingcomputervision.com/")
books.append(item(
    id="RA03B01", cat="03", type="book", material="教材/参考书",
    title="Programming Computer Vision with Python",
    authors="Jan Erik Solem", school="",
    year="2012", version="CC draft（作者站点）",
    level="本科/研究生入门", prereq="Python、线性代数",
    topics="图像处理、局部特征、多视几何入门、三维重建、聚类",
    source="http://programmingcomputervision.com/",
    license="CC 作者草稿",
    goal="机器人视觉入门实践教材（OpenCV 前的算法视图）",
    order=1, out="03_perception/books/Solem_ProgrammingComputerVisionWithPython_CCdraft_en.pdf",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    expect={"title_words": ["Programming", "Computer", "Vision"], "min_pages": 200},
    use="选读",
))

books.append(item(
    id="RA05B01", cat="05", type="book", material="教材/参考书",
    title="Planning Algorithms",
    authors="Steven M. LaValle", school="University of Illinois Urbana-Champaign",
    year="2006", version="Cambridge 2006；作者站点 2012 电子版",
    level="研究生", prereq="算法、线性代数、基础概率",
    topics="构型空间、采样规划、组合规划、决策理论、差动约束、运动规划",
    source="https://lavalle.pl/planning/",
    license="作者允许个人下载电子版；正式版 Cambridge",
    goal="运动规划经典全书",
    order=1, out="05_planning_navigation/books/LaValle_PlanningAlgorithms_2006_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://lavalle.pl/planning/book.pdf",
        "https://msl.cs.illinois.edu/~lavalle/planning/bookbig.pdf",
        "http://lavalle.pl/planning/book.pdf",
    ]},
    expect={"title_words": ["Planning", "Algorithms", "LaValle"], "min_pages": 500},
    cross=["06"],
))

books.append(item(
    id="RA04B03", cat="04", type="book", material="教材/参考书",
    title="Factor Graphs for Robot Perception",
    authors="Frank Dellaert; Michael Kaess", school="Georgia Tech / Carnegie Mellon University",
    year="2017", version="Foundations and Trends in Robotics Vol. 6 (2017)",
    level="研究生", prereq="概率图模型或非线性最小二乘、刚体运动",
    topics="因子图、SAM、稀疏消元、iSAM、Bayes tree、流形优化、SLAM",
    source="https://www.cs.cmu.edu/~kaess/pub/Dellaert17fnt.html",
    license="作者公开 PDF（Now Publishers 专著）",
    goal="现代图优化 SLAM 的标准专著",
    order=3, out="04_localization_mapping/books/DellaertKaess_FactorGraphsRobotPerception_2017_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://www.cs.cmu.edu/~kaess/pub/Dellaert17fnt.pdf",
        "https://dellaert.github.io/21S-8803MM/Readings/Dellaert17fnt.pdf",
    ]},
    expect={"title_words": ["Factor", "Graphs", "Robot", "Perception"], "min_pages": 100},
    cross=["01"],
))

books.append(item(
    id="RA04B04", cat="04", type="book", material="教材/参考书",
    title="SLAM Handbook: From Localization and Mapping to Spatial Intelligence",
    authors="Luca Carlone; Ayoung Kim; Timothy D. Barfoot; Daniel Cremers; Frank Dellaert (eds.)",
    school="MIT / SNU / University of Toronto / TUM / Georgia Tech",
    year="2026", version="public manuscript compiled 2026-04-21",
    level="研究生", prereq="概率机器人、刚体运动、非线性优化",
    topics="因子图、流形、稠密建图、视觉/激光/雷达/IMU、回环、Spatial AI",
    source="https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release",
    license="Cambridge 即将出版；公开稿由编者公开释放",
    goal="2026 年 SLAM 社区手册，覆盖基础到 Spatial AI",
    order=4, out="04_localization_mapping/books/CarloneEtAl_SLAMHandbook_2026_en.pdf",
    get={"kind": "pdf", "max_mb": 250, "urls": [
        "https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release/raw/main/main.pdf",
        "https://asrl.utias.utoronto.ca/~tdb/slam/slamhandbook.pdf",
    ]},
    expect={"title_words": ["SLAM", "Handbook", "Localization"], "min_pages": 200},
    cross=["03", "09"],
))

books.append(item(
    id="RA05B02", cat="05", type="book", material="教材/参考书",
    title="Algorithms for Decision Making",
    authors="Mykel J. Kochenderfer; Tim A. Wheeler; Kyle H. Wray",
    school="Stanford University",
    year="2022", version="MIT Press 2022；作者站点 PDF",
    level="本科高年级/研究生", prereq="多元微积分、线性代数、概率",
    topics="MDP、近似动态规划、在线规划、模仿学习、POMDP、多智能体",
    source="https://algorithmsbook.com/decisionmaking/",
    license="CC BY-NC-ND",
    goal="不确定决策与任务/运动规划算法教材",
    order=2, out="05_planning_navigation/books/Kochenderfer_AlgorithmsForDecisionMaking_2022_en.pdf",
    get={"kind": "pdf", "max_mb": 80, "urls": [
        "https://drive.usercontent.google.com/download?id=1drcYW3iJz4wnnCqjuVwQyc5a6eC7i6cu&export=download",
        "https://algorithmsbook.com/files/dm.pdf",
    ]},
    expect={"title_words": ["Algorithms", "Decision", "Making"], "min_pages": 400},
    cross=["07", "08"],
))

books.append(item(
    id="RA01B03", cat="01", type="book", material="教材/参考书",
    title="Algorithms for Optimization",
    authors="Mykel J. Kochenderfer; Tim A. Wheeler", school="Stanford University",
    year="2019", version="MIT Press 2019；作者站点 PDF",
    level="本科高年级/研究生", prereq="多元微积分、线性代数",
    topics="无约束/约束优化、一阶与二阶方法、采样、代理模型",
    source="https://algorithmsbook.com/optimization/",
    license="CC BY-NC-ND",
    goal="轨迹优化与参数辨识所需的优化算法教材",
    order=3, out="01_mathematical_foundations/books/Kochenderfer_AlgorithmsForOptimization_2019_en.pdf",
    get={"kind": "pdf", "max_mb": 80, "urls": [
        "https://drive.usercontent.google.com/download?id=1Rx7MAekKZbyNVc5B2MNfR0HXXIEJCksp&export=download",
        "https://drive.usercontent.google.com/download?id=1qYjI1igDuBg3x884JKZaCWuJkgdPylHN&export=download",
        "https://algorithmsbook.com/optimization/files/optimization.pdf",
    ]},
    expect={"title_words": ["Algorithms", "Optimization"], "min_pages": 300},
    cross=["05"],
    use="按需查阅",
))

books.append(item(
    id="RA07B01", cat="07", type="book", material="教材/参考书",
    title="Reinforcement Learning: An Introduction (2nd edition)",
    authors="Richard S. Sutton; Andrew G. Barto",
    school="University of Alberta / University of Massachusetts Amherst",
    year="2018", version="2nd ed. 2nd printing 2020 PDF (RLbook2020.pdf)",
    level="本科高年级/研究生", prereq="概率、线性代数、基础编程",
    topics="MDP、动态规划、MC/TD、函数逼近、策略梯度、心理与神经科学联系",
    source="http://incompleteideas.net/book/the-book-2nd.html",
    license="作者公开 PDF；正式版 MIT Press",
    goal="机器人强化学习的标准教材",
    order=1, out="07_learning_embodied_ai/books/SuttonBarto_ReinforcementLearning_2ndEd_2020_en.pdf",
    get={"kind": "pdf", "max_mb": 90, "urls": [
        "http://incompleteideas.net/book/RLbook2020.pdf",
        "https://www.incompleteideas.net/book/RLbook2020.pdf",
    ]},
    expect={"title_words": ["Reinforcement", "Learning", "Sutton"], "min_pages": 400},
    cross=["05"],
))

books.append(item(
    id="RA01B04", cat="01", type="book", material="教材/参考书",
    title="A tutorial on SE(3) transformation parameterizations and on-manifold optimization",
    authors="José-Luis Blanco-Claraco", school="University of Almería",
    year="2010", version="technical report 2010 (rev. later on author site)",
    level="研究生", prereq="线性代数、刚体运动",
    topics="旋转参数化、SE(3)、流形优化、李代数",
    source="https://ingmec.ual.es/~jlblanco/papers/jlblanco2010geometry3D_techrep.pdf",
    license="作者公开技术报告",
    goal="SE(3) 参数化与流形优化的标准技术报告",
    order=4, out="01_mathematical_foundations/books/Blanco_SE3TransformationParameterizations_2010_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://ingmec.ual.es/~jlblanco/papers/jlblanco2010geometry3D_techrep.pdf",
        "https://arxiv.org/pdf/2103.15980.pdf",
    ]},
    expect={"title_words": ["transformation", "manifold"], "min_pages": 40, "min_ratio": 0.4},
    cross=["02", "04"],
    use="通读",
))

books.append(item(
    id="RA05B03", cat="05", type="book", material="教材/参考书",
    title="Introduction to Autonomous Robots (LibreTexts OER edition)",
    authors="Nikolaus Correll", school="University of Colorado Boulder",
    year="2016", version="LibreTexts compiled PDF（OER；非 MIT Press 2022 商业版）",
    level="本科", prereq="线性代数、基础概率、编程",
    topics="运动学、路径规划、传感器、误差传播、定位、SLAM 入门",
    source="https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Autonomous_Robots_(Correll)",
    license="LibreTexts OER（原 CC 开放教材的 OER 再发布）",
    goal="移动机器人本科入门开源教材（LibreTexts 版，不是 2022 年 MIT Press 商业版）",
    order=3, out="05_planning_navigation/books/Correll_IntroductionToAutonomousRobots_LibreTexts_en.pdf",
    get={"kind": "pdf", "max_mb": 80, "urls": [
        "https://batch.libretexts.org/print/Letter/Finished/eng-14766/Full.pdf",
    ]},
    expect={"title_words": ["Autonomous", "Robots"], "min_pages": 80},
    cross=["04", "02"],
    note="MIT Press 2022 商业版作者声明不可公开张贴编译 PDF；此处仅收 LibreTexts 较早 OER 版",
))

books.append(item(
    id="RA02B04", cat="02", type="book", material="教材/参考书",
    title="Robot Dynamics Lecture Notes (HS 2017)",
    authors="Marco Hutter; Roland Siegwart; Robotic Systems Lab",
    school="ETH Zurich",
    year="2017", version="HS 2017 lecture script",
    level="研究生", prereq="理论力学、线性代数",
    topics="旋转与刚体、Jacobian、固定基/浮动基动力学、操作空间控制、足式机器人",
    source="https://rsl.ethz.ch/education-students/lectures/robotdynamics.html",
    license="ETH 课程公开讲义",
    goal="机械臂与浮动基系统动力学建模讲义",
    order=4, out="02_robot_modeling_control/books/ETH_RobotDynamics_HS2017_script_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/rsl-dam/documents/RobotDynamics2017/RD_HS2017script.pdf",
    ]},
    expect={"title_words": ["Robot", "Dynamics"], "min_pages": 40},
    cross=["01", "06"],
    note="讲义脚本按完整教材计一次；ETH 当前学期材料改在 Moodle，本文件为实验室公开的 2017 脚本",
))

g, r = reuse(f"{CSA}/06_learning_control/books/Brunton_DataDrivenScienceEngineering_en.pdf",
             "http://databookuw.com/")
books.append(item(
    id="RA10B01", cat="10", type="book", material="教材/参考书",
    title="Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control",
    authors="Steven L. Brunton; J. Nathan Kutz", school="University of Washington",
    year="2019", version="作者公开 PDF",
    level="研究生", prereq="线性代数、微分方程",
    topics="SVD、DMD、系统辨识、控制中的数据驱动方法",
    source="http://databookuw.com/",
    license="作者公开教学 PDF",
    goal="系统辨识与数据驱动建模，服务仿真到现实",
    order=1, out="10_deployment_applications/books/Brunton_DataDrivenScienceEngineering_en.pdf",
    get=g, reuse=r, cross=["02"],
    note="已有复用：control_systems_automation_literature",
    expect={"title_words": ["Data", "Driven", "Science"], "min_pages": 300},
    use="按需查阅",
))

books.append(item(
    id="RA01B05", cat="01", type="book", material="教材/参考书",
    title="Quaternion kinematics for the error-state Kalman filter",
    authors="Joan Solà", school="IRI / UPC",
    year="2017", version="arXiv 1711.02508",
    level="研究生", prereq="刚体运动、Kalman 滤波",
    topics="四元数、误差状态、IMU 预积分、ESKF",
    source="https://arxiv.org/abs/1711.02508",
    license="arXiv 预印本",
    goal="视觉惯性里程计广泛使用的误差状态 Kalman 教材级教程",
    order=5, out="01_mathematical_foundations/books/Sola_QuaternionKinematicsErrorStateKF_2017_en.pdf",
    get={"kind": "pdf", "urls": ["https://arxiv.org/pdf/1711.02508.pdf"]},
    expect={"title_words": ["Quaternion", "kinematics", "Kalman"], "min_pages": 50},
    cross=["04"],
    note="篇幅达到专著级技术报告，按教材计一次",
))

# =====================================================================
# COURSES
# =====================================================================
g, r = reuse(f"{AI}/courses/MIT_RoboticManipulation_Online_Notes_html_en",
             "https://manipulation.csail.mit.edu/")
courses.append(item(
    id="RA06C01", cat="06", type="course", material="完整文字讲义（官方 HTML 离线包）",
    title="Robotic Manipulation (working notes for MIT 6.4212 / 6.800)",
    authors="Russ Tedrake", school="Massachusetts Institute of Technology",
    year="2024", version="manipulation.csail.mit.edu 当前 HTML（检索日复用源）",
    level="研究生", prereq="线性代数、刚体力学、Python；建议学过欠驱动机器人或最优控制",
    topics="抓取、接触、轨迹优化、感知到动作、Drake 实例",
    source="https://manipulation.csail.mit.edu/",
    license="作者公开讲义",
    goal="机械臂与操作的研究生主课文字讲义",
    order=1, out="06_manipulation/courses/MIT_RoboticManipulation_Online_Notes_html_en",
    get=g, reuse=r, cross=["07", "09"],
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="6.4212 / 6.800", term="MIT 当前学期讲义（持续更新）",
))

g, r = reuse(f"{AI}/courses/MIT_Underactuated_Online_Notes_html_en",
             "https://underactuated.csail.mit.edu/")
courses.append(item(
    id="RA02C01", cat="02", type="course", material="完整文字讲义（官方 HTML 离线包）",
    title="Underactuated Robotics (working notes for MIT 6.8210 / 6.832)",
    authors="Russ Tedrake", school="Massachusetts Institute of Technology",
    year="2024", version="underactuated.csail.mit.edu 当前 HTML",
    level="研究生", prereq="线性代数、常微分方程、基础控制",
    topics="欠驱动系统、轨迹优化、LQR/iLQR、动态规划、强化学习与控制",
    source="https://underactuated.csail.mit.edu/",
    license="作者公开讲义",
    goal="动力学、轨迹优化与欠驱动控制研究生课",
    order=1, out="02_robot_modeling_control/courses/MIT_Underactuated_Online_Notes_html_en",
    get=g, reuse=r, cross=["05", "07"],
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="6.8210 / 6.832", term="MIT 当前学期讲义（持续更新）",
))

g, r = reuse(f"{AI}/courses/Freiburg_MobileRobotics_2023SS_Slides_en",
             "http://ais.informatik.uni-freiburg.de/teaching/ss23/robotics/")
courses.append(item(
    id="RA05C01", cat="05", type="course", material="完整课件包",
    title="Introduction to Mobile Robotics (SS 2023)",
    authors="Wolfram Burgard; Daniel Büscher; et al.",
    school="University of Freiburg",
    year="2023", version="SS 2023 lecture slides",
    level="本科高年级/研究生", prereq="线性代数、概率、编程",
    topics="运动学、传感器、Bayes 滤波、MCL、SLAM、路径规划",
    source="http://ais.informatik.uni-freiburg.de/teaching/ss23/robotics/",
    license="大学公开课件",
    goal="移动机器人定位导航完整课件",
    order=1, out="05_planning_navigation/courses/Freiburg_MobileRobotics_2023SS_Slides_en",
    get=g, reuse=r, cross=["04"],
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="Mobile Robotics", term="SS 2023",
))

g, r = reuse(f"{AI}/courses/Berkeley_CS285_2026Spring_Slides_en",
             "https://rail.eecs.berkeley.edu/deeprlcourse/")
courses.append(item(
    id="RA07C01", cat="07", type="course", material="完整课件包",
    title="CS285 Deep Reinforcement Learning (Spring 2026)",
    authors="Sergey Levine", school="UC Berkeley",
    year="2026", version="Spring 2026 lecture slides",
    level="研究生", prereq="机器学习、强化学习入门",
    topics="策略梯度、Actor-Critic、模型基 RL、离线 RL、机器人学习",
    source="https://rail.eecs.berkeley.edu/deeprlcourse/",
    license="大学公开课件",
    goal="机器人学习方向的深度强化学习主课",
    order=1, out="07_learning_embodied_ai/courses/Berkeley_CS285_2026Spring_Slides_en",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="CS285", term="Spring 2026",
))

g, r = reuse(f"{AI}/courses/Stanford_CS231n_Online_CourseNotes_html_en",
             "https://cs231n.github.io/")
courses.append(item(
    id="RA03C01", cat="03", type="course", material="完整文字讲义（官方 HTML）",
    title="CS231n: Deep Learning for Computer Vision — Course Notes",
    authors="Fei-Fei Li; et al.", school="Stanford University",
    year="2026", version="cs231n.github.io 当前讲义",
    level="本科高年级/研究生", prereq="线性代数、Python、基础机器学习",
    topics="CNN、检测、分割、表征学习",
    source="https://cs231n.github.io/",
    license="课程公开讲义",
    goal="机器人感知所需的深度学习视觉基础",
    order=1, out="03_perception/courses/Stanford_CS231n_Online_CourseNotes_html_en",
    get=g, reuse=r, cross=["07"],
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="CS231n", term="Stanford 当前公开讲义",
))

g, r = reuse(f"{AI}/courses/MIT_6801_2004Fall_OCWCoursePackage_en.zip",
             "https://ocw.mit.edu/courses/6-801-machine-vision-fall-2004/")
courses.append(item(
    id="RA03C02", cat="03", type="course", material="OCW 官方课程包",
    title="6.801/6.866 Machine Vision (Fall 2004)",
    authors="Berthold Horn", school="MIT OpenCourseWare",
    year="2004", version="Fall 2004 OCW package",
    level="研究生", prereq="线性代数、信号处理",
    topics="成像几何、光度、运动、立体",
    source="https://ocw.mit.edu/courses/6-801-machine-vision-fall-2004/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="经典机器视觉完整课程包",
    order=2, out="03_perception/courses/MIT_6801_2004Fall_OCWCoursePackage_en.zip",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="6.801 / 6.866", term="Fall 2004",
))

g, r = reuse(f"{AI}/courses/UCL_RL_Silver_2015_Slides_en",
             "https://www.davidsilver.uk/teaching/")
courses.append(item(
    id="RA07C02", cat="07", type="course", material="完整课件包",
    title="UCL Reinforcement Learning (David Silver, 2015)",
    authors="David Silver", school="University College London / DeepMind",
    year="2015", version="2015 lecture slides",
    level="研究生", prereq="概率、基础机器学习",
    topics="MDP、DP、MC、TD、函数逼近、策略梯度",
    source="https://www.davidsilver.uk/teaching/",
    license="作者公开课件",
    goal="强化学习经典完整课件，衔接机器人学习",
    order=2, out="07_learning_embodied_ai/courses/UCL_RL_Silver_2015_Slides_en",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    course_code="COMPM050 / COMPGI13", term="2015",
))

g, r = reuse(f"{CSA}/05_advanced_control/courses/Stanford_EE363_2026Spring_LectureSlides_en",
             "https://ee363.stanford.edu/")
courses.append(item(
    id="RA04C01", cat="04", type="course", material="完整课件包",
    title="EE363 Linear Dynamical Systems",
    authors="Stephen Boyd", school="Stanford University",
    year="2026", version="Spring 2026 lecture slides",
    level="研究生", prereq="线性代数、线性系统",
    topics="LQR、Kalman 滤波、能观性、线性二次估计",
    source="https://ee363.stanford.edu/",
    license="课程公开课件",
    goal="Kalman 滤波与线性估计的标准研究生课件",
    order=1, out="04_localization_mapping/courses/Stanford_EE363_2026Spring_LectureSlides_en",
    get=g, reuse=r, cross=["02"],
    note="已有复用：control_systems_automation_literature",
    course_code="EE363", term="Spring 2026",
))

courses.append(item(
    id="RA02C02", cat="02", type="course", material="OCW 官方课程包",
    title="2.12 Introduction to Robotics (Fall 2005)",
    authors="Harry Asada; John Leonard", school="MIT OpenCourseWare",
    year="2005", version="Fall 2005",
    level="本科", prereq="动力学、微分方程",
    topics="平面与空间运动学、机构、动力学、力控制、实验",
    source="https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/",
    license="CC BY-NC-SA 4.0（MIT OCW）",
    goal="机械臂本科导论完整课程包（含 Asada 讲义章节）",
    order=2, out="02_robot_modeling_control/courses/MIT_212_2005Fall_OCWCoursePackage_en.zip",
    get={"kind": "file", "max_mb": 400, "urls": [
        "https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/2.12-fall-2005.zip",
        "https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/resources/2-12-fall-2005.zip",
    ]},
    expect={"min_docs": 8, "link_check": False, "must_have": ["2\\.12|introduction|robotics|chapter"]},
    course_code="2.12", term="Fall 2005",
    cross=["06"],
))

courses.append(item(
    id="RA03C03", cat="03", type="course", material="完整课件包",
    title="Vision Algorithms for Mobile Robotics (Fall 2025)",
    authors="Davide Scaramuzza", school="University of Zurich / ETH Zurich",
    year="2025", version="Fall 2025 lecture slides",
    level="研究生", prereq="线性代数、几何、矩阵微积分",
    topics="相机模型与标定、特征、多视几何、光流、视觉惯性融合、SLAM 导引",
    source="https://rpg.ifi.uzh.ch/teaching.html",
    license="课程公开课件",
    goal="移动机器人视觉算法完整课件（UZH/ETH 核心课）",
    order=3, out="03_perception/courses/UZH_VAMR_2025Fall_Slides_en",
    get={"kind": "pdfset", "min_files": 8, "urls": [
        "https://rpg.ifi.uzh.ch/docs/teaching/2025/01_introduction.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2025/02_image_formation.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/01_introduction.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/02_image_formation_1.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/03_camera_calibration.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/04_filtering.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/05_point_feature_detection_1.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/06_point_feature_detection_2.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/07_multiple_view_geometry_1.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/08_multiple_view_geometry_2.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/09_multiple_view_geometry_3.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/10_multiple_view_geometry_4.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/11_optical_flow.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/12_place_recognition.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2024/13_visual_inertial_fusion.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/01_introduction.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/02_image_formation_1.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/03_image_formation_2.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/04_image_filtering.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/05_point_feature_detection_1.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/06_point_feature_detection_2.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/07_multiple_view_geometry_1.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/08_multiple_view_geometry_2.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/09_multiple_view_geometry_3.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/10_multiple_view_geometry_4.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/11_optical_flow.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/12a_place_recognition.pdf",
        "https://rpg.ifi.uzh.ch/docs/teaching/2023/13_visual_inertial_fusion.pdf",
    ]},
    expect={"min_pages": 1, "title_words": []},
    course_code="VAMR", term="Fall 2025",
    cross=["04"],
    note="Fall 2026 学期进行中，完整年度课件取 2025 完整套；不收无人机专项研讨课",
))

courses.append(item(
    id="RA05C02", cat="05", type="course", material="完整文字讲义",
    title="Principles of Robot Autonomy (AA274A/AA174A notes, 2024–25)",
    authors="Gioele Zardini; Joseph Lorenzetti; Marco Pavone",
    school="Stanford University",
    year="2024", version="2024-09-24 lecture notes PDF",
    level="本科高年级/研究生", prereq="CS 106A 或同等编程；CME 100 微积分线性代数；CME 106 概率",
    topics="移动机器人运动学、轨迹优化、图搜索与采样规划、相机、滤波定位、SLAM、ROS 导引",
    source="https://stanfordasl.github.io/PoRA-I/aa174a_aut2425/",
    license="Stanford ASL 公开讲义",
    goal="自主导航完整文字讲义（规划-感知-决策栈）",
    order=2, out="05_planning_navigation/courses/Stanford_AA274A_2024_LectureNotes_en.pdf",
    get={"kind": "pdf", "urls": [
        "https://stanfordasl.github.io/PoRA-I/aa174a_aut2425/pdfs/AA_PoRA_lecture_notes_2425.pdf",
        "https://stanfordasl.github.io/PoRA-I/aa174a_aut2324/pdfs/AA_PoRA_lecture_notes.pdf",
    ]},
    expect={"title_words": ["Principles", "Robot", "Autonomy"], "min_pages": 80},
    course_code="AA274A / AA174A", term="Autumn 2024–25",
    cross=["04", "09"],
))

courses.append(item(
    id="RA01C01", cat="01", type="course", material="完整文字讲义（扫描笔记包）",
    title="16-811 Math Fundamentals for Robotics (Fall 2025 notes)",
    authors="Michael Erdmann", school="Carnegie Mellon University",
    year="2025", version="handwritten lecture notes posted for Fall 2025",
    level="研究生", prereq="线性代数、微积分；机器人入门有帮助",
    topics="线性方程、逼近、非线性方程、优化、变分、构型空间、微分几何",
    source="https://www.cs.cmu.edu/~me/811/",
    license="作者允许个人复制；注明来源",
    goal="机器人数学基础研究生课讲义",
    order=1, out="01_mathematical_foundations/courses/CMU_16811_MathFundamentalsRobotics_Notes_en",
    get={"kind": "pdfset", "index": "https://www.cs.cmu.edu/~me/courses/811/notes/handouts.html",
         "pattern": r"811/notes/[^\"']+\.pdf|/(Linear|Polynomials|Roots|Resultants|Approximation|DiffEq|Optimization|Variations|Markov|CSpace|Convex|Voronoi|DifferentialGeometry|Topology)[^\"']*\.pdf",
         "min_files": 8},
    expect={"min_pages": 1, "allow_scan": True, "title_words": []},
    course_code="16-811", term="Fall 2025",
    note="手写扫描讲义；作者声明可供个人使用，广泛传播需注明出处",
))

courses.append(item(
    id="RA04C02", cat="04", type="course", material="完整课件包",
    title="Photogrammetry I & II (2021/22)",
    authors="Cyrill Stachniss", school="University of Bonn",
    year="2021", version="2021/22 lecture slides",
    level="本科高年级/研究生", prereq="线性代数、几何",
    topics="相机模型、对极几何、三角化、光束法平差、Kalman、EKF-SLAM",
    source="https://www.ipb.uni-bonn.de/photo12-2021/",
    license="作者公开课件（允许教学使用并保留致谢）",
    goal="视觉几何与 SLAM 入门的完整课件",
    order=2, out="04_localization_mapping/courses/Bonn_Photogrammetry_2021_Slides_en",
    get={"kind": "pdfset", "index": "https://www.ipb.uni-bonn.de/photo12-2021/index.html",
         "pattern": r"https://www\.ipb\.uni-bonn\.de/[^\"']+\.pdf",
         "min_files": 10},
    expect={"min_pages": 1, "title_words": []},
    course_code="Photogrammetry I & II", term="2021/22",
    cross=["03"],
))

courses.append(item(
    id="RA04C03", cat="04", type="course", material="完整课件包",
    title="Mobile Sensing and Robotics 2 (Spring 2021)",
    authors="Cyrill Stachniss", school="University of Bonn",
    year="2021", version="Spring 2021 lecture slides",
    level="研究生", prereq="概率、线性代数、Photogrammetry 或同等",
    topics="最小二乘、ICP、图优化 SLAM、激光与视觉定位",
    source="https://www.ipb.uni-bonn.de/msr2-2021/",
    license="作者公开课件",
    goal="SLAM 与点云配准完整课件",
    order=3, out="04_localization_mapping/courses/Bonn_MSR2_2021_Slides_en",
    get={"kind": "pdfset", "index": "https://www.ipb.uni-bonn.de/msr2-2021/index.html",
         "pattern": r"https://www\.ipb\.uni-bonn\.de/[^\"']+\.pdf|msr2-2021/[^\"']+\.pdf",
         "min_files": 6},
    expect={"min_pages": 1, "title_words": []},
    course_code="MSR2", term="Spring 2021",
    cross=["03"],
))

# =====================================================================
# TOOLS
# =====================================================================
tools.append(item(
    id="RA09T01", cat="09", type="docs", material="官方 HTML 离线包",
    tool="ROS 2", title="ROS 2 Jazzy — Concepts, Tutorials, How-to Guides (core)",
    authors="Open Robotics / ROS 2 documentation contributors",
    school="Open Robotics", year="2026",
    version="Jazzy Jalisco 文档站点当前版（检索日）",
    level="本科/工程", prereq="Linux、Python 或 C++ 基础",
    topics="节点、话题、服务、动作、参数、生命周期、tf2、rosbag2 录制回放",
    source="https://docs.ros.org/en/jazzy/",
    license="ROS 2 文档许可（项目官方）",
    goal="ROS 2 通信、坐标变换、录制回放的官方入门与核心概念",
    order=1, out="09_software_simulation/tools/ROS2_Jazzy_ConceptsTutorials_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://docs.ros.org/en/jazzy/Concepts.html",
        "https://docs.ros.org/en/jazzy/Tutorials.html",
        "https://docs.ros.org/en/jazzy/How-To-Guides.html",
        "https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools.html",
        "https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries.html",
        "https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html",
        "https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html",
        "https://docs.ros.org/en/jazzy/Concepts/Basic/About-ROS-2-Client-Libraries.html",
        "https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Tf2.html",
        "https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Parameters.html",
        "https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Lifecycle.html",
    ], "domains": ["docs.ros.org"], "include": ["/en/jazzy"],
        "level": "3", "quota_mb": 120, "timeout": 2400, "wait": 0.4,
        "exclude": ["/en/jazzy/p/", "/en/jazzy/Installation/Releases"]},
    expect={"min_docs": 8, "link_check": False},
    complete="部分",
    scope="Jazzy：Concepts、Tutorials（CLI/客户端库/tf2/录制回放）、How-to 索引及一级页面；不含发行版安装包、完整 API 参考历史版本",
    note="ROS 2 LTS 取 Jazzy（2024-05 至 2029-05）。Humble 仍在维护但不作本包主体。不收 ROS 1。",
    stack="ROS 2 Jazzy",
))

tools.append(item(
    id="RA09T02", cat="09", type="docs", material="官方 HTML 离线包",
    tool="Gazebo", title="Gazebo documentation (Harmonic / current docs hub)",
    authors="Open Robotics / Gazebo contributors", school="Open Robotics",
    year="2026", version="gazebosim.org/docs 当前版",
    level="本科/工程", prereq="ROS 2 基础或独立仿真概念",
    topics="世界、模型、传感器、插件、与 ROS 2 桥接",
    source="https://gazebosim.org/docs",
    license="项目官方文档",
    goal="Gazebo 仿真官方用户指南（入门与核心概念）",
    order=2, out="09_software_simulation/tools/Gazebo_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://gazebosim.org/docs",
        "https://gazebosim.org/docs/harmonic/getstarted",
        "https://gazebosim.org/docs/harmonic/overview",
    ], "domains": ["gazebosim.org"], "include": ["/docs"],
        "level": "3", "quota_mb": 80, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
    complete="部分",
    scope="文档中心与 Harmonic 入门/概览及一级链接；不含大型场景资源",
    stack="Gazebo Harmonic（与 ROS 2 Jazzy 配对）",
    note="Garden 已结束。Ionic 对应 Kilted。本包以 Harmonic/Jazzy 配对为主。",
))

tools.append(item(
    id="RA09T03", cat="09", type="docs", material="官方 HTML 离线包",
    tool="MuJoCo", title="MuJoCo documentation (Read the Docs current)",
    authors="Google DeepMind", school="Google DeepMind",
    year="2026", version="mujoco.readthedocs.io 当前稳定文档",
    level="研究生/工程", prereq="刚体动力学概念、Python 或 C",
    topics="MJCF、仿真步进、接触、传感器、Python 绑定、可视化",
    source="https://mujoco.readthedocs.io/",
    license="项目官方文档",
    goal="MuJoCo 用户指南与核心 API 说明",
    order=3, out="09_software_simulation/tools/MuJoCo_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://mujoco.readthedocs.io/en/stable/",
        "https://mujoco.readthedocs.io/en/stable/overview.html",
        "https://mujoco.readthedocs.io/en/stable/programming.html",
        "https://mujoco.readthedocs.io/en/stable/python.html",
        "https://mujoco.readthedocs.io/en/stable/XMLreference.html",
    ], "domains": ["mujoco.readthedocs.io"],
        "level": "3", "quota_mb": 80, "timeout": 1800, "wait": 0.3},
    expect={"min_docs": 10, "link_check": False},
    complete="部分",
    scope="stable 文档：概述、编程、Python、XML 参考及一级页面",
    stack="MuJoCo",
))

tools.append(item(
    id="RA09T04", cat="09", type="docs", material="官方 HTML 离线包",
    tool="Isaac Lab", title="Isaac Lab documentation (current GitHub Pages)",
    authors="NVIDIA", school="NVIDIA",
    year="2026", version="isaac-sim.github.io/IsaacLab 当前版",
    level="研究生/工程", prereq="Python、强化学习或机器人仿真基础",
    topics="环境、任务、域随机化、训练工作流、与 Isaac Sim 关系",
    source="https://isaac-sim.github.io/IsaacLab/",
    license="项目官方文档",
    goal="Isaac Lab 用户指南（仿真训练框架，不是 Isaac Sim 安装包）",
    order=4, out="09_software_simulation/tools/IsaacLab_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://isaac-sim.github.io/IsaacLab/main/index.html",
        "https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html",
        "https://isaac-sim.github.io/IsaacLab/main/source/tutorials/index.html",
        "https://isaac-sim.github.io/IsaacLab/main/source/overview/index.html",
    ], "domains": ["isaac-sim.github.io"], "include": ["/IsaacLab"],
        "level": "3", "quota_mb": 100, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
    complete="部分",
    scope="Isaac Lab 文档站点入门、安装说明、教程与概述；不含 Isaac Sim 安装包、资源包、模型权重",
    stack="Isaac Lab / Isaac Sim",
    note="Isaac Sim 是仿真应用，Isaac Lab 是基于其上的学习/任务框架。不下载软件本体。",
    cross=["07", "10"],
))

tools.append(item(
    id="RA09T05", cat="09", type="docs", material="官方 HTML 离线包",
    tool="MoveIt 2", title="MoveIt 2 documentation and tutorials (main)",
    authors="PickNik / MoveIt maintainers", school="PickNik Robotics",
    year="2026", version="moveit.picknik.ai/main 当前版",
    level="本科高年级/工程", prereq="ROS 2、机械臂运动学概念",
    topics="运动规划、规划场景、运动学插件、与 ros2_control 接口",
    source="https://moveit.picknik.ai/main/index.html",
    license="项目官方文档",
    goal="MoveIt 2 用户指南与教程（ROS 2，不是 MoveIt 1）",
    order=5, out="09_software_simulation/tools/MoveIt2_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://moveit.picknik.ai/main/index.html",
        "https://moveit.picknik.ai/main/doc/tutorials/tutorials.html",
        "https://moveit.picknik.ai/main/doc/concepts/concepts.html",
    ], "domains": ["moveit.picknik.ai"], "include": ["/main"],
        "level": "3", "quota_mb": 80, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
    complete="部分",
    scope="MoveIt 2 main 文档的概念与教程；不含 MoveIt 1",
    stack="MoveIt 2 + ROS 2",
    cross=["05", "06"],
))

tools.append(item(
    id="RA09T06", cat="09", type="docs", material="官方 HTML 离线包",
    tool="Nav2", title="Nav2 documentation (current)",
    authors="Open Navigation / Nav2 maintainers", school="Open Navigation",
    year="2026", version="docs.nav2.org 当前版",
    level="本科高年级/工程", prereq="ROS 2、移动机器人导航概念",
    topics="行为树导航、代价地图、规划器、控制器、定位、路线图",
    source="https://docs.nav2.org/",
    license="项目官方文档",
    goal="Nav2 用户指南与核心概念（ROS 2 导航栈）",
    order=6, out="09_software_simulation/tools/Nav2_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://docs.nav2.org/",
        "https://docs.nav2.org/concepts/index.html",
        "https://docs.nav2.org/tutorials/index.html",
        "https://docs.nav2.org/configuration/index.html",
        "https://docs.nav2.org/plugin_tutorials/index.html",
    ], "domains": ["docs.nav2.org"],
        "level": "3", "quota_mb": 80, "timeout": 1800, "wait": 0.3},
    expect={"min_docs": 10, "link_check": False},
    complete="部分",
    scope="概念、教程、配置与插件教程；不含仿真地图数据包",
    stack="Nav2 + ROS 2",
    cross=["05"],
))

tools.append(item(
    id="RA09T07", cat="09", type="docs", material="官方 HTML 离线包",
    tool="Pinocchio", title="Pinocchio documentation (current)",
    authors="Guilhem Saurel; Justin Carpentier; et al. (Stack of Tasks / Inria)",
    school="Inria / Stack of Tasks",
    year="2026", version="stack-of-tasks.github.io/pinocchio 当前版",
    level="研究生/工程", prereq="刚体动力学、C++ 或 Python",
    topics="刚体算法、正逆动力学、导数、URDF、Python 绑定",
    source="https://stack-of-tasks.github.io/pinocchio/",
    license="项目官方文档",
    goal="Pinocchio 刚体动力学库用户指南",
    order=7, out="09_software_simulation/tools/Pinocchio_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://stack-of-tasks.github.io/pinocchio/",
        "https://gepettoweb.laas.fr/doc/stack-of-tasks/pinocchio/master/doxygen-html/",
    ], "domains": ["stack-of-tasks.github.io", "gepettoweb.laas.fr"],
        "span": True, "level": "2", "quota_mb": 80, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False},
    complete="部分",
    scope="项目主页与 Doxygen 入门/模块页；完整 API 不无限抓取历史版本",
    stack="Pinocchio",
    cross=["01", "02"],
))

tools.append(item(
    id="RA09T08", cat="09", type="docs", material="官方 HTML 离线包",
    tool="Drake", title="Drake documentation (current)",
    authors="Russ Tedrake; Robot Locomotion Group / TRI",
    school="MIT / Toyota Research Institute",
    year="2026", version="drake.mit.edu 当前版",
    level="研究生/工程", prereq="Python 或 C++、刚体动力学、优化",
    topics="多体、轨迹优化、系统框架、传感器、仿真",
    source="https://drake.mit.edu/",
    license="项目官方文档",
    goal="Drake 模型基设计与仿真用户指南",
    order=8, out="09_software_simulation/tools/Drake_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://drake.mit.edu/",
        "https://drake.mit.edu/getting_started.html",
        "https://drake.mit.edu/python_bindings.html",
        "https://drake.mit.edu/doxygen_cxx/index.html",
    ], "domains": ["drake.mit.edu"],
        "level": "2", "quota_mb": 100, "timeout": 1800, "wait": 0.4,
        "exclude": ["/pydrake", "/doxygen_cxx/class", "/doxygen_cxx/struct"]},
    expect={"min_docs": 8, "link_check": False},
    complete="部分",
    scope="入门、Python 绑定、Doxygen 索引；不含完整逐类 API 无限展开",
    stack="Drake",
    cross=["02", "06"],
))

g, r = reuse(f"{PRG}/official_docs/opencv_5.0.0_docs_html_en.zip",
             "https://github.com/opencv/opencv/releases/download/5.0.0/opencv-5.0.0-docs.zip")
tools.append(item(
    id="RA03T01", cat="03", type="docs", material="官方文档",
    tool="OpenCV", title="OpenCV 5.0.0 官方文档（Doxygen HTML 包）",
    authors="OpenCV team", school="OpenCV",
    year="2026", version="5.0.0",
    level="本科/工程", prereq="Python 或 C++",
    topics="图像处理、标定、特征、视频、DNN 模块",
    source="https://docs.opencv.org/5.0.0/",
    license="Apache-2.0",
    goal="机器人感知常用视觉库完整官方文档包",
    order=1, out="03_perception/tools/opencv_5.0.0_docs_html_en.zip",
    get=g, reuse=r,
    note="已有复用：programming_reference_literature",
    stack="OpenCV 5.0.0",
    expect={"min_docs": 10, "link_check": False},
))

tools.append(item(
    id="RA04T01", cat="04", type="docs", material="官方 HTML 离线包",
    tool="GTSAM", title="GTSAM documentation (current)",
    authors="Frank Dellaert; Georgia Tech / borglab",
    school="Georgia Institute of Technology",
    year="2026", version="gtsam.org 当前版",
    level="研究生/工程", prereq="因子图概念、C++ 或 Python",
    topics="因子图、非线性优化、IMU、SLAM 示例",
    source="https://gtsam.org/",
    license="BSD（库）；文档随项目",
    goal="GTSAM 用户指南与入门",
    order=1, out="04_localization_mapping/tools/GTSAM_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://gtsam.org/",
        "https://gtsam.org/get_started/",
        "https://gtsam.org/tutorials/intro.html",
        "https://gtsam-jlblanco-docs.readthedocs.io/en/latest/",
    ], "domains": ["gtsam.org", "gtsam-jlblanco-docs.readthedocs.io"],
        "span": True, "level": "3", "quota_mb": 60, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 5, "link_check": False},
    complete="部分",
    scope="官方站点入门/教程及社区 ReadTheDocs 导引",
    stack="GTSAM",
    cross=["01"],
))

tools.append(item(
    id="RA05T01", cat="05", type="docs", material="官方 HTML 离线包",
    tool="OMPL", title="OMPL documentation (current)",
    authors="Kavraki Lab / OMPL developers", school="Rice University",
    year="2026", version="ompl.kavrakilab.org 当前版",
    level="研究生/工程", prereq="运动规划概念、C++",
    topics="采样规划、状态空间、规划器、基准",
    source="https://ompl.kavrakilab.org/",
    license="项目官方文档",
    goal="OMPL 运动规划库用户指南",
    order=1, out="05_planning_navigation/tools/OMPL_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://ompl.kavrakilab.org/",
        "https://ompl.kavrakilab.org/core/api_overview.html",
        "https://ompl.kavrakilab.org/core/education.html",
        "https://ompl.kavrakilab.org/gui.html",
    ], "domains": ["ompl.kavrakilab.org"],
        "level": "3", "quota_mb": 80, "timeout": 1800, "wait": 0.4},
    expect={"min_docs": 8, "link_check": False},
    complete="部分",
    scope="核心概述、API 概览、教学与 GUI 文档",
    stack="OMPL",
))

tools.append(item(
    id="RA03T02", cat="03", type="docs", material="官方 HTML 离线包",
    tool="Open3D", title="Open3D documentation (current)",
    authors="Intel ISL / Open3D team", school="Intel ISL",
    year="2026", version="www.open3d.org/docs 当前稳定版",
    level="本科高年级/工程", prereq="Python、点云概念",
    topics="点云、网格、可视化、配准、重建",
    source="https://www.open3d.org/docs/",
    license="项目官方文档",
    goal="Open3D 点云与三维处理用户指南",
    order=2, out="03_perception/tools/Open3D_Docs_html_en.tar",
    get={"kind": "mirror", "start": [
        "https://www.open3d.org/docs/release/",
        "https://www.open3d.org/docs/release/getting_started.html",
        "https://www.open3d.org/docs/release/tutorial/index.html",
        "https://www.open3d.org/docs/release/python_api/index.html",
    ], "domains": ["www.open3d.org"], "include": ["/docs/release"],
        "level": "3", "quota_mb": 80, "timeout": 1800, "wait": 0.3},
    expect={"min_docs": 10, "link_check": False},
    complete="部分",
    scope="release 文档：入门、教程、Python API 索引；不含数据集",
    stack="Open3D",
))

# =====================================================================
# PRACTICE
# =====================================================================
g, r = reuse(f"{AI}/practice/MIT_Manipulation_repo_en",
             "https://github.com/RussTedrake/manipulation")
practice.append(item(
    id="RA06X01", cat="06", type="practice", material="官方课程仓库",
    title="MIT Robotic Manipulation 课程仓库（讲义源码、notebook 与习题）",
    authors="Russ Tedrake", school="MIT",
    year="2026", version="复用源已核验的仓库快照",
    level="研究生", prereq="Python、Drake 概念、刚体运动",
    topics="抓取、轨迹优化、notebook 习题",
    source="https://github.com/RussTedrake/manipulation",
    license="仓库内 LICENSE",
    goal="操作课程配套代码与习题（不执行）",
    order=1, out="06_manipulation/practice/MIT_Manipulation_repo_en",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    stack="Drake / Python",
    expect={"need_license": True, "min_docs": 3},
))

g, r = reuse(f"{AI}/practice/MIT_Underactuated_repo_en",
             "https://github.com/RussTedrake/underactuated")
practice.append(item(
    id="RA02X01", cat="02", type="practice", material="官方课程仓库",
    title="MIT Underactuated Robotics 课程仓库（讲义源码、notebook 与习题）",
    authors="Russ Tedrake", school="MIT",
    year="2026", version="复用源已核验的仓库快照",
    level="研究生", prereq="Python、最优控制概念",
    topics="轨迹优化、LQR、notebook 习题",
    source="https://github.com/RussTedrake/underactuated",
    license="仓库内 LICENSE",
    goal="欠驱动课程配套代码与习题（不执行）",
    order=1, out="02_robot_modeling_control/practice/MIT_Underactuated_repo_en",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    stack="Drake / Python",
    expect={"need_license": True, "min_docs": 3},
))

g, r = reuse(f"{AI}/practice/Freiburg_MobileRobotics_2023SS_Exercises_en",
             "http://ais.informatik.uni-freiburg.de/teaching/ss23/robotics/")
practice.append(item(
    id="RA05X01", cat="05", type="practice", material="课程习题包",
    title="Freiburg Introduction to Mobile Robotics SS2023 exercises",
    authors="AIS Freiburg", school="University of Freiburg",
    year="2023", version="SS 2023 exercises",
    level="本科高年级", prereq="Python、概率、线性代数",
    topics="运动模型、滤波、定位习题",
    source="http://ais.informatik.uni-freiburg.de/teaching/ss23/robotics/",
    license="课程公开材料",
    goal="移动机器人课程习题（不执行）",
    order=1, out="05_planning_navigation/practice/Freiburg_MobileRobotics_2023SS_Exercises_en",
    get=g, reuse=r,
    note="已有复用：ai_undergraduate_graduate_curriculum_literature",
    expect={"min_docs": 1},
))

g, r = reuse(f"{PRG}/practice/opencv_5.0.0_samples_en.tar",
             "https://github.com/opencv/opencv")
practice.append(item(
    id="RA03X01", cat="03", type="practice", material="官方示例源码",
    title="OpenCV 5.0.0 samples",
    authors="OpenCV team", school="OpenCV",
    year="2026", version="5.0.0 samples（大于 5MB 数据已剔除）",
    level="本科/工程", prereq="Python 或 C++",
    topics="标定、特征、立体、DNN 示例",
    source="https://github.com/opencv/opencv",
    license="Apache-2.0",
    goal="OpenCV 官方示例（不执行）",
    order=1, out="03_perception/practice/opencv_5.0.0_samples_en.tar",
    get=g, reuse=r,
    note="已有复用：programming_reference_literature",
    stack="OpenCV 5.0.0",
    expect={"need_license": False, "min_docs": 1},
))

practice.append(item(
    id="RA02X02", cat="02", type="practice", material="官方示例源码归档",
    title="Modern Robotics code library (NxRLab/ModernRobotics)",
    authors="Kevin Lynch; Northwestern students", school="Northwestern University",
    year="2024", version="官方仓库 depth-1（sparse: 代码与许可证）",
    level="本科/研究生", prereq="Python 或 MATLAB、Modern Robotics 教材",
    topics="正逆运动学、动力学、轨迹生成示例",
    source="https://github.com/NxRLab/ModernRobotics",
    license="仓库 LICENSE",
    goal="教材配套参考实现（不执行）",
    order=2, out="02_robot_modeling_control/practice/NxRLab_ModernRobotics_code_en.tar",
    get={"kind": "git", "repo": "https://github.com/NxRLab/ModernRobotics.git",
         "paths": ["README.md", "LICENSE", "packages", "doc"]},
    expect={"need_license": True, "min_docs": 2, "must_have": ["README"]},
    stack="Python / MATLAB",
    cross=["01"],
))

practice.append(item(
    id="RA09X01", cat="09", type="practice", material="官方示例源码归档",
    title="ros2/examples (ROS 2 official examples)",
    authors="Open Robotics", school="Open Robotics",
    year="2026", version="官方仓库 examples（默认分支 depth-1）",
    level="本科/工程", prereq="ROS 2 概念",
    topics="rclcpp/rclpy 节点、话题、服务、动作、参数、启动文件",
    source="https://github.com/ros2/examples",
    license="Apache-2.0",
    goal="ROS 2 官方示例（不执行、不安装）",
    order=1, out="09_software_simulation/practice/ros2_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/ros2/examples.git",
         "paths": ["README.md", "LICENSE", "rclcpp", "rclpy", "launch_testing"]},
    expect={"need_license": True, "min_docs": 2, "must_have": ["rclpy|rclcpp"]},
    stack="ROS 2",
))

practice.append(item(
    id="RA06X02", cat="06", type="practice", material="官方教程源码归档",
    title="MoveIt 2 tutorials repository",
    authors="PickNik / MoveIt maintainers", school="PickNik",
    year="2026", version="moveit2_tutorials 默认分支 depth-1",
    level="本科高年级/工程", prereq="ROS 2、MoveIt 2 概念",
    topics="规划场景、运动规划、正逆解调用示例",
    source="https://github.com/moveit/moveit2_tutorials",
    license="BSD-3-Clause",
    goal="MoveIt 2 官方教程源码（剔除大型网格；不执行）",
    order=2, out="06_manipulation/practice/moveit2_tutorials_en.tar",
    get={"kind": "git", "repo": "https://github.com/moveit/moveit2_tutorials.git",
         "paths": ["README.md", "LICENSE", "doc"]},
    expect={"need_license": True, "min_docs": 3},
    stack="MoveIt 2 + ROS 2",
    cross=["09"],
))

practice.append(item(
    id="RA05X02", cat="05", type="practice", material="官方教程源码归档",
    title="Nav2 documentation/tutorials sources (navigation2)",
    authors="Open Navigation", school="Open Navigation",
    year="2026", version="navigation2 默认分支，sparse doc/nav2_bringup",
    level="本科高年级/工程", prereq="ROS 2、Nav2 概念",
    topics="导航启动、参数、示例启动文件",
    source="https://github.com/ros-navigation/navigation2",
    license="Apache-2.0",
    goal="Nav2 官方仓库中的文档与 bringup 示例（不含地图数据集）",
    order=2, out="05_planning_navigation/practice/nav2_docs_bringup_en.tar",
    get={"kind": "git", "repo": "https://github.com/ros-navigation/navigation2.git",
         "paths": ["README.md", "LICENSE", "doc", "nav2_bringup", "nav2_simple_commander"]},
    expect={"need_license": True, "min_docs": 2},
    stack="Nav2 + ROS 2",
    cross=["09"],
))

practice.append(item(
    id="RA02X03", cat="02", type="practice", material="官方示例源码归档",
    title="Pinocchio examples",
    authors="Stack of Tasks / Inria", school="Inria",
    year="2026", version="官方仓库 examples 目录",
    level="研究生", prereq="Python、刚体动力学",
    topics="正逆动力学、URDF 加载示例",
    source="https://github.com/stack-of-tasks/pinocchio",
    license="BSD-2-Clause",
    goal="Pinocchio 官方示例（不执行）",
    order=3, out="02_robot_modeling_control/practice/pinocchio_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/stack-of-tasks/pinocchio.git",
         "paths": ["README.md", "COPYING.LESSER", "LICENSE", "examples", "doc"]},
    expect={"need_license": True, "min_docs": 2, "must_have": ["examples"]},
    stack="Pinocchio",
))

practice.append(item(
    id="RA06X03", cat="06", type="practice", material="官方示例源码归档",
    title="Drake manipulation examples (RobotLocomotion/drake examples/manipulation)",
    authors="Russ Tedrake; Drake developers", school="MIT / TRI",
    year="2026", version="官方仓库 sparse examples/manipulation + LICENSE",
    level="研究生", prereq="Python、Drake 文档",
    topics="操作站、夹爪、相机示例",
    source="https://github.com/RobotLocomotion/drake",
    license="BSD-3-Clause",
    goal="Drake 操作示例（不执行，剔除大型资源）",
    order=3, out="06_manipulation/practice/drake_manipulation_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/RobotLocomotion/drake.git",
         "paths": ["README.md", "LICENSE", "examples/manipulation", "tutorials"]},
    expect={"need_license": True, "min_docs": 2},
    stack="Drake",
    cross=["09"],
))

practice.append(item(
    id="RA04X01", cat="04", type="practice", material="官方示例源码归档",
    title="GTSAM examples",
    authors="borglab / Georgia Tech", school="Georgia Tech",
    year="2026", version="官方仓库 examples 目录",
    level="研究生", prereq="C++ 或 Python、因子图",
    topics="位姿图、IMU、SLAM 小示例",
    source="https://github.com/borglab/gtsam",
    license="BSD-3-Clause",
    goal="GTSAM 官方示例（不执行）",
    order=1, out="04_localization_mapping/practice/gtsam_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/borglab/gtsam.git",
         "paths": ["README.md", "LICENSE", "examples", "python/gtsam/examples"]},
    expect={"need_license": True, "min_docs": 2, "must_have": ["examples"]},
    stack="GTSAM",
))

practice.append(item(
    id="RA05X03", cat="05", type="practice", material="官方示例源码归档",
    title="OMPL demos",
    authors="Kavraki Lab", school="Rice University",
    year="2026", version="官方仓库 demos 目录",
    level="研究生", prereq="C++、运动规划概念",
    topics="采样规划器演示",
    source="https://github.com/ompl/ompl",
    license="BSD-3-Clause",
    goal="OMPL 官方演示（不执行）",
    order=3, out="05_planning_navigation/practice/ompl_demos_en.tar",
    get={"kind": "git", "repo": "https://github.com/ompl/ompl.git",
         "paths": ["README.md", "LICENSE", "demos", "doc"]},
    expect={"need_license": True, "min_docs": 2, "must_have": ["demos"]},
    stack="OMPL",
))

practice.append(item(
    id="RA03X02", cat="03", type="practice", material="官方示例源码归档",
    title="Open3D examples",
    authors="Intel ISL / Open3D team", school="Intel ISL",
    year="2026", version="官方仓库 examples 目录",
    level="本科高年级/工程", prereq="Python",
    topics="点云处理、配准、可视化示例",
    source="https://github.com/isl-org/Open3D",
    license="MIT",
    goal="Open3D 官方示例（剔除大型数据）",
    order=2, out="03_perception/practice/open3d_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/isl-org/Open3D.git",
         "paths": ["README.md", "LICENSE", "examples", "docs/jupyter"]},
    expect={"need_license": True, "min_docs": 2, "must_have": ["examples"]},
    stack="Open3D",
))

practice.append(item(
    id="RA09X02", cat="09", type="practice", material="官方示例源码归档",
    title="ros2_control demos",
    authors="ros-controls maintainers", school="ros-controls",
    year="2026", version="ros2_control_demos 默认分支",
    level="工程", prereq="ROS 2、控制接口概念",
    topics="硬件接口、控制器、示例机器人",
    source="https://github.com/ros-controls/ros2_control_demos",
    license="Apache-2.0",
    goal="ros2_control 官方演示（不执行、不装仿真）",
    order=2, out="09_software_simulation/practice/ros2_control_demos_en.tar",
    get={"kind": "git", "repo": "https://github.com/ros-controls/ros2_control_demos.git"},
    expect={"need_license": True, "min_docs": 2},
    stack="ros2_control + ROS 2",
    cross=["02"],
))

practice.append(item(
    id="RA07X01", cat="07", type="practice", material="官方参考项目（源码，无权重）",
    title="LeRobot (Hugging Face) — library, configs, examples (no model weights)",
    authors="Hugging Face LeRobot team", school="Hugging Face",
    year="2026", version="官方仓库 depth-1，剔除权重大文件",
    level="研究生/工程", prereq="Python、PyTorch、强化学习或模仿学习概念",
    topics="数据集接口、策略训练脚本、仿真环境封装",
    source="https://github.com/huggingface/lerobot",
    license="Apache-2.0",
    goal="具身学习参考实现（不下载权重、不执行）",
    order=1, out="07_learning_embodied_ai/practice/huggingface_lerobot_src_en.tar",
    get={"kind": "git", "repo": "https://github.com/huggingface/lerobot.git",
         "paths": ["README.md", "LICENSE", "lerobot", "examples", "docs", "pyproject.toml"]},
    expect={"need_license": True, "min_docs": 3, "must_have": ["lerobot"]},
    stack="LeRobot / PyTorch",
    note="fetch 会丢弃超过阈值的权重/数据文件；不运行代码",
    cross=["10"],
))

practice.append(item(
    id="RA08X01", cat="08", type="practice", material="官方示例源码归档",
    title="ROS 2 tf2 examples / geometry2 (tf2 tutorial code)",
    authors="Open Robotics", school="Open Robotics",
    year="2026", version="geometry2 仓库 tutorials 与 README",
    level="本科/工程", prereq="ROS 2",
    topics="坐标变换广播与监听示例",
    source="https://github.com/ros2/geometry2",
    license="BSD",
    goal="多坐标系/多机器人定位所需的 tf2 示例（不执行）",
    order=1, out="08_multi_robot/practice/ros2_geometry2_tf2_examples_en.tar",
    get={"kind": "git", "repo": "https://github.com/ros2/geometry2.git",
         "paths": ["README.md", "LICENSE", "tf2", "tf2_ros", "tf2_ros_py", "docs"]},
    expect={"need_license": True, "min_docs": 2},
    stack="ROS 2 tf2",
    cross=["09", "04"],
))


def dump(name, rows):
    path = SEEDS / name
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {len(rows):3d} -> {path.name}")


def main():
    SEEDS.mkdir(parents=True, exist_ok=True)
    ids = [x["id"] for x in books + courses + tools + practice]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"duplicate ids: {sorted(dup)}")
    dump("B_books_en.json", books)
    dump("C_courses_en.json", courses)
    dump("T_tools_en.json", tools)
    dump("X_practice_en.json", practice)
    print("books", len(books), "courses", len(courses), "tools", len(tools), "practice", len(practice))


if __name__ == "__main__":
    main()
