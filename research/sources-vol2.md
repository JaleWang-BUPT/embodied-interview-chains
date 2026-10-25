# 卷二题源存证与链接状态（2026-10-26）

> 卷二审查 round 1 发现 8 个牛客实录帖在发布前复核时已删（详情页"内容不存在"）。本文件按"死链不进实录行、证据先归档"的原则存证：每帖记录调研阶段（2026-10-26 上午，经牛客搜索索引交叉确认过标题/作者/日期）获得的题目引用原文，供回溯。发布时实录行只挂当前可访问的 URL；已删帖以本文件（GitHub 永久链接）为存证引用。

## 已删帖存证（8 帖）

### 1. 安克·具身智能算法面经（策略梯度链唯一实录源 → C01；MPC 后三层 → C09）
- 原 URL：https://www.nowcoder.com/feed/main/detail/81c435929b9b4476b06d2b17d6c7d8a3 （已删）
- 调研记录：牛客837298194号（山东大学），2026-02-26 发布、2026-03-03 编辑
- 调研阶段引用的题目原文：「1. 策略梯度公式」「为什么能对期望求导？」「2. 策略梯度方差很大怎么办？」「baseline为什么可以降低方差，会不会引入偏差？」（帖主自答要点："无偏性：baseline不依赖于动作a"）「4. baseline有哪些类型」「如果机械臂抓取任务，哪种更加合适？」（帖主自答："用状态价值V(s)作为baseline就足够了"）
- 同帖另含 MPC 链：「6. MPC的原理」「和LQR、PID的区别」「7. MPC实时应用中如何保证求解速度」「8. 求解失败怎么办」「qpOASES与OSQP对比」

### 2. 牛客·强化学习（运动控制方向）面经（PPO 链 → C02）
- 原 URL：https://www.nowcoder.com/feed/main/detail/8bb49b11b68f42f6af0e5d5d9733c332 （已删）
- 调研记录：不看可惜了（门头沟学院·深度学习），2025-09-25
- 题目引用：「1. PPO的原理是什么？」「2. on-policy和off-policy的区别」「3. Importance sampling, why use it」「4. ppo loss 组成」「5. 可以只用一个total loss同时更新两个网络吗？」（帖主自答："不应公用一个loss，logP项只需更新actor，value项只需更新critic"）

### 3. 牛客·具身智能RL面经（一面+二面）（reward 链 → C05）
- 原 URL：https://www.nowcoder.com/feed/main/detail/85b7648839a34b78ab5e1ec336592f64 （已删）
- 调研记录：来点小蛋糕（南京邮电大学），2026-01-22
- 题目引用：「reward 有哪些？回报是Reward吗？」「reward hacking怎么处理？」「reward的权重如何调整」「AMP是自己实现的还是用的开源的」

### 4. 牛客·人形机器人公司（银河通用）面经（一帖四家 → C06/C16）
- 原 URL：https://www.nowcoder.com/feed/main/detail/08d1e542d1ac4db5a99c2a2f47dd9219 （已删）
- 调研记录：lietou文森（北京邮电大学），2026-03-25；帖主声明"都是我被面试过程中面试官所提问的"
- 题目引用：银河通用「model-free vs model-based RL 区别」（自答："model-based会去学习动力学模型，采样效率高但有模型误差"）「offline vs online RL」（自答："offline数据集是固定的"）；上海人形「灵巧手：力控相关」「调reward的细节」；北京人形（评论区）「1. 真机上用RL成功吗？ 2. sim2real gap怎么解决？ 3. 为什么用模仿学习？」

### 5. 牛客·智元 运动控制算法一面（RL vs 传统控制 → C08）
- 原 URL：https://www.nowcoder.com/feed/main/detail/67877c8af36848d59b2c95d99873a90d （已删）
- 调研记录：来点小蛋糕（南京邮电大学），2026-03-18
- 题目引用：「强化学习和传统控制各自的优势，如何选择？」「系统的性能指标如何评价？（时域分析、频域分析、超调量、稳定时间、相位裕度等等）」

### 6. 牛客·智元 三天三轮面经（三环控制链唯一实录源 → C10）
- 原 URL：https://www.nowcoder.com/feed/main/detail/b32824297c194914b28af2e433dcf0a10 （已删）
- 调研记录：只想躺平的蚌埠人（西安电子科技大学），2026-09-14
- 题目引用：「电流环、速度环、位置环怎么嵌套？为什么要外面套一环？内环的频率一定要比外环高吗？」「PID先调哪个？」（自答：内环先调）「1kHz的控制频率，PID 0.2ms，执行器延迟5ms，怎么补偿？」「传感器数据抖动，怎么滤波？」「卡尔曼滤波的Q和R怎么调？」

### 7. 牛客·腿部强化学习面试记录（腿足链唯一实录源 → C07）
- 原 URL：https://www.nowcoder.com/feed/main/detail/f72297eb56304348823be586a7c94434 （已删）
- 调研记录：来点小蛋糕（南京邮电大学），2026-05-11
- 题目引用：「腿部串并联的设计」「为什么不在训练的时候做action smoothing，如果要做的话可以怎么做？」「heading correction为什么这么做」「陀螺仪数据如何处理」（自答含"滤波带来的延迟和误差会不会影响训练"）「obs action的镜像问题」「对称loss的作用」「腿解算是怎么做的」
- 另一已删腿足帖《牛客 腿足强化学习面经 大复盘》（2025-12-23，https://www.nowcoder.com/feed/main/detail/25b9bb5064b34937bc48238cd85a2434 ）：搜索快照含「指令怎么映射到目标姿态」「为什么滤波了但是不会影响网络的输出」

### 8. 牛客·智元 算法实习一面（LADRC 链唯一实录源 → C15）
- 原 URL：https://www.nowcoder.com/feed/main/detail/93c9e5e75969435393982564e8926e90 （已删）
- 调研记录：来点小蛋糕（南京邮电大学），2026-03-06
- 题目引用：「为什么选择LADRC，不用pid」「误差减小的百分比是指什么」「和强化学习怎么结合，强化学习是你做的吗」

### 另：已删帖（题单调研期已记录，非本轮新发现）
- 《牛客 强化学习和传统控制结合的一些问题》（2026-03-01，https://www.nowcoder.com/feed/main/detail/f2fbd3f56381446385250418ea997465 ）：搜索快照四问「强化学习和传统控制的比例怎么分」「pid是怎么设计的」「时域分析和频域分析」「最看重的一个指标」

## 当前可访问来源（2026-10-26 维护者复核）

| 来源 | URL | 状态 |
|---|---|---|
| 牛客·云鲸 具身智能算法校招面经 | https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d | ✅ 匿名可读（PPO on/off policy、重要性采样、GAE 数字题、训练诊断原题均在正文） |
| 牛客·秋招记录(9) 安克创新机器人控制算法一面 | https://www.nowcoder.com/feed/main/detail/679003b65a1a404c9e1d755e7e1c4fd7 | ✅（"lqr、pid、mpc 三种控制方法的区别"原题；2024-10 发布、2026-10 编辑。MPC 实时性/求解失败/qpOASES vs OSQP 三层见已删安克帖存证 #1） |
| 牛客·TPLink 提前批（机器人算法）面经 | https://www.nowcoder.com/feed/main/detail/f79996d0300d4b60957770816bb0ace5 | ✅（VMC 六问） |
| GitHub·Cgxiaoxin/Embodied_Learning 面试复盘 | https://github.com/Cgxiaoxin/Embodied_Learning/blob/main/interview/面试复盘.md | ✅（赛博格/湃特纳/零次方/iData/地瓜等场次） |
| 知乎·具身智能面经（二）——强化学习篇 | https://zhuanlan.zhihu.com/p/2082240221471576304 | ✅（reward 设计、sim2real/DR、offline/online；作者声明"整理自我的实际面试经历"，按〔整理〕计） |
| 知乎·2026 秋招仿真+强化学习控制岗指南（Xbotics） | https://zhuanlan.zhihu.com/p/2054527428802900763 | ✅（分层控制、先 SysID 再 DR；社区指南，语境参考不计频） |
| GitHub·offerseed #6 | https://github.com/offerseed/interview-experience/issues/6 | ✅（RL 基础/引入 RL/action chunk 一步定义；语境参考不计频） |

Wayback Machine 在复核时段对以上已删 URL 限流未能查询（archive.org 429）；如后续发现快照可补入本文件。
