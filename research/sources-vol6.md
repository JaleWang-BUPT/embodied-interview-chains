# 卷六题源记录（2026-10-26）

## 一手原帖

- 作者：HenryZhou_（公开页面署名）。
- 标题：阿里系面经—三维重建/SLAM。
- 日期：2024-04-09 20:51；核验于 2026-10-26，web open 可读正文。
- URL：https://www.nowcoder.com/feed/main/detail/057f10b935f545dbad249a1a62e987e4
- C02：高德场次第3–6题依次是高斯误差、MVS/NeRF点云比较、tile覆盖近似、PyTorch/CUDA四线性插值。短摘录：「高斯重建的主要误差来自于哪里」「高斯球占据的tile近似计算」。
- C03：智能信息场次第2/3题含体素编码、进化算法、项目输入输出、NeRF预训练、位姿、SLAM、RGB/mesh、单物体/大场景及实际可用。短摘录：「输入输出是什么」「NeRF是个预训练好的网络吗」「SLAM还能估计位姿？」
- 原帖未提供候选人的实现或参考答案。正文给出独立技术回答与准备框架，不伪称知道其项目细节。单作者不因两个场次而扩大同一链频次。
- 搜索中发现把这段问答改归“蚂蚁数字人”的汇总页，非一手且公司归属与原作者不同，未采用。

## 题单待核

C01 在原题单标“跨维”，但原 URL/作者/日期没有落盘；不能独立确认一手面经。全链已降为推断练习，保留已审题目范围，不计频次。

## 技术校核

- [OpenCV solvePnP](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)：3D–2D、物体到相机的变换、EPnP与内参/畸变。
- [OpenCV 标定 API](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)：相机模型、畸变参数与标定/重投影误差。
- [3DGS 作者 rasterizer](https://github.com/graphdeco-inria/diff-gaussian-rasterization/blob/main/cuda_rasterizer/forward.cu)：屏幕协方差、最大特征值、3σ圆半径及tile矩形裁剪。不是精确椭圆逐tile相交测试。
- [NeRF 原始项目](https://www.matthewtancik.com/nerf)：以图像和相机位姿优化场景表示、沿射线渲染。

技术材料不计面经频次；题目中的“四线性”按四维多线性解释，实际面试应先确认维度和边界条件。
