# 卷一题源与修订边界（2026-10-26）

旧卷曾把博客整理、prep指南和未留外部快照的题单都计入实录频次。本轮撤销这些未经逐层核实的频次；保留问题作为练习，不因URL存在或历史审查文字就认定面试真实发生。

## 当前主题锚点

- [offerseed #6](https://github.com/offerseed/interview-experience/issues/6)，N0TPO3T，2026-09-29；正文可读。C08采用低频推理/动作执行及RTC与ensemble主题，C11采用离线指标与真机结果背离、第一次optimizer.step显存溢出主题。主题重排，非原帖连续同一链；本卷具体作答及扩展问题均标推断。
- [Cgxiaoxin复盘](https://github.com/Cgxiaoxin/Embodied_Learning/blob/main/interview/%E9%9D%A2%E8%AF%95%E5%A4%8D%E7%9B%98.md)，作者Cgxiaoxin，页面更新2026-07-03、单场日期未知；本轮会话先前已全文读到，旧卷复检后续GitHub/raw请求404，记录访问时点差异而不称持续可读。C12采用浙江滴石场次插值/拟合与均值窗口主题，不把所有工程回答冒称现场答案。

## 技术校正依据（不是面试频次证据）

- [π0原始论文](https://www.physicalintelligence.company/download/pi0.pdf)：动作频率不等于调用频率；state/action专家权重分流、机器人数据训练。C01/C03。
- [π*0.6 / RECAP官方说明](https://www.pi.website/blog/pistar06)：区分π0.6基座和后训练版本，不将ensemble作为版本定义。C02/C15。
- [ACT官方实现](https://github.com/tonyzhaozh/act/blob/main/policy.py)：L1+加权KL，无图像重建辅助损失；ACT本身是BC。C06。
- [Flow Matching论文](https://arxiv.org/abs/2210.02747)、[DDIM论文](https://arxiv.org/abs/2010.02502)：条件路径、向量场与采样随机性须区分；C02/C07。
- [RTC官方说明](https://www.pi.website/research/real_time_chunking)：生成中的延迟/前缀约束，不是简单事后平均；C08。
- [UniVLA论文](https://arxiv.org/abs/2505.06111)：从视觉变化学习潜在动作，不等同直接量化已标注动作；C13。
- [Qwen2.5-VL官方说明](https://qwenlm.github.io/blog/qwen2.5-vl/)：ViT window attention版本归属；C16。

## 逐链历史引用台账

以下是修订前已保存的引用，作为历史检索线索，不声称本轮全部可读、原题逐字一致或来源独立。每条C编号对应正文同编号；未经当前主题锚点覆盖的题目层全部推断，工程答案是本仓库独立撰写。

### C01

[牛客·VLA面经分享](https://www.nowcoder.com/feed/main/detail/7b8f541c9bef4733a0f738d0628b1f65)、[牛客·小米一面](https://www.nowcoder.com/feed/main/detail/6eb5c7ced0d346679cb77aa2d5e691bc)、CSDN《具身智能VLA面经总结（小鸡毛版）》（[链接](https://blog.csdn.net/2303_77547168/article/details/161990436)）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C02

[牛客·VLA算法实习面经](https://www.nowcoder.com/feed/main/detail/a17ad61fa5d6433881915334973f5354)、[牛客·VLA面经分享](https://www.nowcoder.com/feed/main/detail/7b8f541c9bef4733a0f738d0628b1f65)

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C03

CSDN《与 π0 有关的面试题总结》（[链接](https://blog.csdn.net/qq_41920323/article/details/162309012)）、CSDN《具身智能VLA面经总结（小鸡毛版）》（[链接](https://blog.csdn.net/2303_77547168/article/details/161990436)）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C04

CSDN《π0.5 的面试考点》（[链接](https://blog.csdn.net/qq_41920323/article/details/162684495)）、CSDN《pi0.5面试题》（[链接](https://blog.csdn.net/m0_62493032/article/details/162701672)）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C05

CSDN《具身智能TL常用算法面经》系列（[（二）](https://blog.csdn.net/lovely_yoshino/article/details/160722050)，同作者 4 篇计 1）、CSDN《与 π0 有关的面试题总结》（[链接](https://blog.csdn.net/qq_41920323/article/details/162309012)）、CSDN《从ROS通信到生成模型》（[链接](https://blog.csdn.net/m0_51738372/article/details/160307298)）、CSDN《为什么说flow matching diversity表达不足…》（[链接](https://blog.csdn.net/weixin_43332715/article/details/148759368)）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C06

[牛客·VLA算法实习面经](https://www.nowcoder.com/feed/main/detail/a17ad61fa5d6433881915334973f5354)（ACT 流程实录）、CSDN《TL常用算法面经（四）》（[链接](https://blog.csdn.net/lovely_yoshino/article/details/160743611)，模拟追问链）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C07

CSDN《为什么说flow matching diversity表达不足…》（[链接](https://blog.csdn.net/weixin_43332715/article/details/148759368)，技术博客）、CSDN《从ROS通信到生成模型》（[链接](https://blog.csdn.net/m0_51738372/article/details/160307298)）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C08

[牛客·VLA面经分享](https://www.nowcoder.com/feed/main/detail/7b8f541c9bef4733a0f738d0628b1f65)（3Hz/50Hz、抖动原题）、[牛客·VLA算法实习](https://www.nowcoder.com/feed/main/detail/a17ad61fa5d6433881915334973f5354)（RTC 实现追问）、[牛客·云鲸](https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d)（RTC 参数）、GitHub [offerseed #6](https://github.com/offerseed/interview-experience/issues/6)（ensemble vs RTC 选型）

本轮分档：仅认可上文所述主题锚点，其余扩展推断。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C09

CSDN《具身智能VLA面经总结（小鸡毛版）》（[链接](https://blog.csdn.net/2303_77547168/article/details/161990436)，LoRA/PEFT 类）；迁移排查层为整理归纳〔推断〕

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C10

CSDN《具身智能VLA面经总结（小鸡毛版）》（[链接](https://blog.csdn.net/2303_77547168/article/details/161990436)，训练与评测类）、[gankinterview 具身智能面试考点](https://www.gankinterview.cn/blog/embodied-ai-interview-when-large-models-are-integrated-into-robots-what-new-know)（Perplexity 原题）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C11

GitHub [offerseed #6](https://github.com/offerseed/interview-experience/issues/6)（指标背离、OOM 原题）、CSDN《具身智能TL常用算法面经》（[链接](https://xingyun3d.csdn.net/69fb0c350a2f6a37c5a812f8.html)，debug 五层，整理）

本轮分档：仅认可上文所述主题锚点，其余扩展推断。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C12

GitHub [Cgxiaoxin 面试复盘·浙江滴石](https://github.com/Cgxiaoxin/Embodied_Learning/blob/main/interview/%E9%9D%A2%E8%AF%95%E5%A4%8D%E7%9B%98.md)（确认式追问全记录）

本轮分档：仅认可上文所述主题锚点，其余扩展推断。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C13

[牛客·傅利叶一面](https://www.nowcoder.com/feed/main/detail/37af3ac1986b438c81cd26ab90a792a8)（四层深挖全记录）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C14

[牛客·具身算法一面](https://www.nowcoder.com/feed/main/detail/ece59d44599042c39696b3b1114bb3b4)；追问 1 借用卷五"技术选型攻击"模式

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C15

CSDN《具身智能VLA面经总结（小鸡毛版）》（[链接](https://blog.csdn.net/2303_77547168/article/details/161990436)，VLA 与世界模型类）；知乎《2026 秋招，仿真+强化学习控制岗到底需要什么能力？》（[链接](https://zhuanlan.zhihu.com/p/2054527428802900763)，语境参考不计频）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C16

[牛客·千寻智能一面](https://www.nowcoder.com/feed/main/detail/fe79ba8a8d36464c96261292dcadccc4)〔卷积参数组为推断补全，公式为通用知识〕

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。

### C17

[techinterview.net Physical Intelligence 指南](https://www.techinterview.net/blog/physical-intelligence-pi-interview-guide)（英文 prep 站，无实录追问链，降权收录）

本轮分档：全链推断；旧记录未取得足够逐层外证，旧频次撤销。上述原记录中的“全记录”“原题”“实录”等措辞不代表本轮核验结论。
