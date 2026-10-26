# 卷二题源存证与链接状态（2026-10-26）

> 下列旧题录是本仓库早期调研自记，非独立第三方网页快照；“已删”“原题”及可读状态均为当时记录，不是本轮已独立证实的事实。本轮无法取得外部原文的题层已降为推断，不据此认领公司、连续追问或频次。GitHub main链接仅是可变记录入口，不是原网页永久存档。

## 历史题录（原记录称8帖已删，本轮未独立确认）

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

## 早期访问台账（历史状态，不代表持续可读）

| 来源 | URL | 当时记录的状态 |
|---|---|---|
| 牛客·云鲸 具身智能算法校招面经 | https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d | ✅ 匿名可读（PPO on/off policy、重要性采样、GAE 数字题、训练诊断原题均在正文） |
| 牛客·秋招记录(9) 安克创新机器人控制算法一面 | https://www.nowcoder.com/feed/main/detail/679003b65a1a404c9e1d755e7e1c4fd7 | ✅（"lqr、pid、mpc 三种控制方法的区别"原题；2024-10 发布、2026-10 编辑。MPC 实时性/求解失败/qpOASES vs OSQP 三层见已删安克帖存证 #1） |
| 牛客·TPLink 提前批（机器人算法）面经 | https://www.nowcoder.com/feed/main/detail/f79996d0300d4b60957770816bb0ace5 | ✅（VMC 六问） |
| GitHub·Cgxiaoxin/Embodied_Learning 面试复盘 | https://github.com/Cgxiaoxin/Embodied_Learning/blob/main/interview/面试复盘.md | ✅（赛博格/湃特纳/零次方/iData/地瓜等场次） |
| 知乎·具身智能面经（二）——强化学习篇 | https://zhuanlan.zhihu.com/p/2082240221471576304 | ✅（reward 设计、sim2real/DR、offline/online；作者声明"整理自我的实际面试经历"，按〔整理〕计） |
| 知乎·2026 秋招仿真+强化学习控制岗指南（Xbotics） | https://zhuanlan.zhihu.com/p/2054527428802900763 | ✅（分层控制、先 SysID 再 DR；社区指南，语境参考不计频） |
| GitHub·offerseed #6 | https://github.com/offerseed/interview-experience/issues/6 | ✅（RL 基础/引入 RL/action chunk 一步定义；语境参考不计频） |

Wayback Machine 在复核时段对以上已删 URL 限流未能查询（archive.org 429）；如后续发现快照可补入本文件。

## 本轮发布复检的访问差异

- [云鲸canonical](https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d) 对部分请求只有导航；独立附录审查在2026-10-26打开 [sourceSSR变体](https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d?sourceSSR=dynamic) 取得正文，署名网络冲浪十级选手兼潜水冠军，显示02-26 15:25，年份未显示。短摘录“ppo原理，同策略和异策略有什么区别，ppo属于哪种？”“重要性采样是什么，为什么ppo要用重要性采样？”。C02主问及重要性采样概念有锚点；旧记录另称有GAE数字题/末段精控及policy/value loss诊断，但本轮未独立复现这些具体原题；C03/C04全链降为推断练习，不认领云鲸场次。
- 独立旧卷审查本轮读取 [安克秋招9](https://www.nowcoder.com/feed/main/detail/679003b65a1a404c9e1d755e7e1c4fd7) 正文，短摘录“lqr、pid、mpc 三种控制方法的区别”，只支持C09主问主题，不支持求解器三层追问；原记录日期2024-10发布、2026-10编辑，作者本轮未确认。
- [TPLink](https://www.nowcoder.com/feed/main/detail/f79996d0300d4b60957770816bb0ace5) 本轮旧卷审查读到正文，署名/原日期本轮未确认。原题先问VMC原理/为何用、sim2real，随后问PPO算法改进，再转到学校项目的遥操作延迟与量化指标。C06仅采用sim2real主题，C14不能把后段所有问题绑定成VMC实验；改为推断接法/指标练习。
- Cgxiaoxin复盘本轮会话先前已取得全文，记录于卷三至卷五题源；旧卷复检的后续GitHub内容/匿名raw请求均404。此时点差异不否定先前已读内容，也不证明永久可读或已删除。页面更新2026-07-03，单场日期未知；同作者多场仍是一份复盘，正文不报告整链频次。
- 知乎208224…本轮旧卷复检403，旧台账的“作者声明真实经历”不替代当前原文。未取得外部快照的层全部保守推断。Wayback未取证不证明原帖存在或删除。

## 逐链采用范围

以下表的“工程展开”均由本仓库独立撰写，每层行内标推断；认可主题不等于认可整个拼接链的实录顺序。所有旧频次撤销，不将可访问次数当独立面经次数。

### C01

历史题录§1；全链推断。

### C02

云鲸主问/重要性采样有正文；loss、总loss及具体梯度说明为推断，历史题录§2不算外部证据。

### C03

历史GAE数字与精控题单，本轮没有独立原文证据，全链推断。

### C04

历史policy/value loss诊断题单，本轮没有独立原文证据，全链推断。

### C05

历史题录§3及未重新取得原文的知乎；全链推断。

### C06

TPLink的sim2real与会话先前Cg地瓜主题；随机化范围、real2sim资产与案例为推断。

### C07

历史题录§7；全链推断，不认领串并联到滤波的连续现场。

### C08

历史题录§5与另记f2f…；全链推断，PID设计是工程练习。

### C09

安克秋招9仅LQR/PID/MPC比较；实时性、fallback、求解器三层推断。

### C10

历史题录§6；全链推断，保留原记录5ms为延迟而非更新周期。

### C11

会话先前Cg赛博格的误差/URDF/辨识/摩擦主题，跨场合并；激励、可辨识性与物理一致为工程展开。

### C12

会话先前Cg湃特纳的IK/臂角、零次方的Pinocchio、iData冗余解主题；适用构型与几何流程推断。

### C13

会话先前Cg iData的阻抗/导纳、形变/冗余主题；公式与稳定性边界为工程展开。

### C14

TPLink主题顺序如上；PPO-VMC绑定、遥操作方案和指标归属均推断。

### C15

历史题录§8；全链推断，不以自记证明智元原题。

### C16

历史题录§4与未取回知乎；全链推断，撤去各公司固定考法宣称。

## 技术依据（不计面经频次）

审查末轮追加（2026-10-26）：旧卷审查代理以匿名curl读取同一云鲸sourceSSR变体的HTML，确认帖子自身的content字段含GAE λ=.95第10步、末段1秒精控及policy/value loss诊断题，而非相关推荐或AI解答。前文“未独立复现”描述的是此前正文抽取器阶段；不同工具得到的正文状态有差异。正文C03/C04仍保守保留推断练习，不恢复频次，也不把帖主回答当作技术依据；追加证据和核验限度见vol2_round5审查记录。

- [GAE原论文](https://arxiv.org/abs/1506.02438)：λ偏差/方差，不按末段秒数直接定取值。
- [PPO原论文](https://arxiv.org/abs/1707.06347)：surrogate、价值/熵项与clip边界。
- [AMP原论文](https://arxiv.org/abs/2104.02180)：运动状态转移先验，而非只对动作向量做判别。
- [MIT机器人课程控制说明](https://manipulation.csail.mit.edu/force.html)：力/位置接口、阻抗和接触控制的条件。

数值与控制例子是限定假设下的学习材料，不构成真机稳定性证明或安全控制方案。

## 维护者提供场次（2026-10-27）

两条一手面试题清单由维护者直接提供：**原帖链接待补**。题目文本仅作主题锚点，作答与展开逐层推断，不冒称现场作答、不据清单计频。

### 落位

- 原力灵机 VLA+RL 组：Q19 从最终效果确认 advantage 生效、Q20 RECAP Value Model 输入输出、Q21 30% 阈值来源、Q25 离线训练与在线分布偏移 → C17；Q22 稀疏奖励缓解、Q23 失败样本与人工纠正轨迹使用 → C18；Q24 RL Token 效果与适用性 → C17 追问 4
- 银河通用：Q3 GRPO 优点 → C19；Q7 RLT 压缩信息损失 → C17 追问 4；Q6 训练时 vs 推理时 RTC → 卷一 C20（跨卷）
- 银河通用其余问题（LeRobot、降采样滤波、Flow Matching 公式、π0.5 vs OpenVLA、触觉模态、推理排查）落位见 [卷一题源](https://github.com/JaleWang-BUPT/embodied-interview-chains/blob/main/research/sources-vol1.md)。

### C17（题面原文组）

「怎样从最终效果确认 advantage 生效」「RECAP Value Model 的输入输出是什么」「Advantage 的 30% 阈值是怎样得到的」「RECAP 离线训练与在线行为分布偏移怎样处理」「RL Token 方法的效果和适用性如何」（含追问：压缩时丢失了多少信息）。

### C18（题面原文组）

「稀疏奖励可能失效，怎样缓解」「失败样本和人工纠正轨迹怎样使用」。

### C19（题面原文）

「讲一下 GRPO 的优点」。
