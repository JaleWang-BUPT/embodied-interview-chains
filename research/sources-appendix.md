# 手撕附录题源与实现范围（2026-10-26）

## 可追溯题目

- [offerseed #6](https://github.com/offerseed/interview-experience/issues/6)，N0TPO3T，2026-09-29；GitHub正文可读。第一轮15短摘录“多头自注意力”，覆盖C01主问及mask检查；第二轮15含条件Flow Matching、有效动作掩码、Euler和最小测试，覆盖C02四层。C01单头/KV cache/FlashAttention延伸标推断。
- [辉羲智能面经](https://www.nowcoder.com/feed/main/detail/57033fe8898b4e85b97c48d8b2dcfb28)，署名匿名牛油，2025-03-27 14:57；独立审查代理于2026-10-26直接读到正文，三面短摘录“手撕softmax算子”。匿名署名不视作跨帖稳定身份。C03只以该主问为实录锚点，温度与全mask标推断。
- [宇树嵌入式面经索引](https://www.nowcoder.com/discuss/919881358401372160?sourceSSR=dynamic)，题名《27宇树嵌入式面经凉经》，作者/原日期本轮未取回。独立审查代理于2026-10-26检索 `"27宇树嵌入式面经凉经" "卷积"` 取得索引短摘录：“手撕：实现一个二维卷积的朴素版本，然后问怎么优化”“手撕追问：循环顺序换一下为什么会快，跟 cache 有什么关系”。分别覆盖C04主问、追1、追2；具体尺寸约定为工程作答。canonical详情只返回导航外壳，主代理另用ID搜索未复现，因此只认可该次索引证据，不声称完整网页归档；营销相似来源不累加频次。
- C07早期参考过 [卷二题目存证 §2](https://github.com/JaleWang-BUPT/embodied-interview-chains/blob/main/research/sources-vol2.md)：原帖8bb49b…已删，存证记作者不看可惜了、2025-09-25，短摘录“PPO的原理是什么？”“Importance sampling, why use it”。存证是本仓库历史调研记录，并非独立第三方快照；不能作为独立原题证据；C07概念层最终采用下方本轮实际读到的云鲸变体，手写要求、符号与detach为推断练习，不新增频次。原先采用的 [云鲸链接](https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d) 在卷二曾记录可读，但本轮仅返回导航，未取得原题全文，不继续称当前可读。
- C06的Q/R问题见 [卷二题目存证](https://github.com/JaleWang-BUPT/embodied-interview-chains/blob/main/research/sources-vol2.md)，旧记录称原智元帖已删，本轮没有独立外证确认删除或原题。没有独立存证证明KF题面，全链（含Q/R追问）标推断，不补计实录频次。

## 本轮追加访问核验

独立审查代理在上述canonical核验之后，于2026-10-26直接打开 `sourceSSR=dynamic` 变体取得正文。访问路径/缓存差异不能笼统推广成“所有详情均可读”：

- [宇树成功变体](https://www.nowcoder.com/discuss/919881358401372160?sourceSSR=dynamic)：署名“已注销”，显示08-20 09:20（年份未显示）；正文含上面两条卷积原题。页面含专栏推广，保留来源质量警示，不重复计频次。
- [云鲸成功变体](https://www.nowcoder.com/feed/main/detail/b18ddc5475694fc0bcedc07f9764d10d?sourceSSR=dynamic)：署名网络冲浪十级选手兼潜水冠军，显示02-26 15:25（年份未显示）；短摘录“ppo原理，同策略和异策略有什么区别，ppo属于哪种？”“重要性采样是什么，为什么ppo要用重要性采样？”。仅证明C07概念层有公开问题依据，不证明手写要求。C07概念层正文改引此成功变体，历史题录仅留检索线索，不凭访问次数增加频次。

## 没有原题外证的练习

C05早期PD/抗饱和/旋转/牛顿链未留URL；C08只留链表/第k大/路径标签，完整题面未知。两链全标推断。未保留“纯机器人创业公司不考coding”等无统计证据的概括。

## 实现与测试

- examples/learning.py：无偏置的多头self-attention、有效动作masked MSE、直线路径条件FM、Euler采样、PPO actor项。
- examples/handwritten.py：稳定softmax、单通道valid互相关、标量PID条件积分、Z旋转、牛顿迭代、标量KF、链表/堆/BFS。
- tests：对照PyTorch SDPA，检查因果/全mask/梯度、FM时间方向、PPO正负优势clip；标准库例子检查数值不变量与失败分支。

代码只实现注明的子问题，不含生产控制保护、完整RL rollout或完整VLA训练。测试通过只能证明覆盖用例下的行为，不能证明机器人稳定或完整算法性能。

## 维护者提供场次（2026-10-27）

原力灵机手撕组由维护者直接提供：**原帖链接待补**。题目文本仅作主题锚点；伪代码风格、RTC 复用细节与实现由本仓库独立编写，标推断。

### C09（题面原文组）

「写一个带 KV Cache 的自回归注意力伪代码」「写出 Training-time RTC 场景中 KV Cache 复用的伪代码」。实现边界与测试口径见 examples/ 与 tests/，不声称对应原面试者写法。

## 原帖检索结果（2026-10-27）

- 原力灵机场次原帖（三面记录，同场次吻合、无逐题清单）见 [卷一题源](https://github.com/JaleWang-BUPT/embodied-interview-chains/blob/main/research/sources-vol1.md)；C09 逐题明细仍为维护者提供文本，原帖链接待补。
