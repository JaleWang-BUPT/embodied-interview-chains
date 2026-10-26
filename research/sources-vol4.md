# 卷四题源与证据边界（2026-10-26）

本卷沿用已审题单的 14 条链，答案独立撰写。以下区分实际读取原帖、作者动态摘要、搜索索引、以及仅有题单记录；HTTP 200 只表示请求完成，不能证明正文存在。

## 直接原始记录

- [Cgxiaoxin 面试复盘](https://github.com/Cgxiaoxin/Embodied_Learning/blob/main/interview/%E9%9D%A2%E8%AF%95%E5%A4%8D%E7%9B%98.md)：2026-10-26 经 GitHub contents API 读取全文。安努多相机动态标定与量化精度；地瓜 ROS1/2、DDS、接口选型和 FP8；湃特纳 shared_ptr、RAII、进程线程。覆盖 C01/C09/C10/C14。同一作者仓库只算一个独立来源。
- [莱修贤动态](https://www.nowcoder.com/users/159227329)：网页正文可见银河两场原作者记录；一面 union/struct 与大小，二面 ROS、手眼、Socket 四问。覆盖 C10/C11/C12/C14。二面详情 https://www.nowcoder.com/feed/main/detail/202d73d6968b458389a738ba0d70e6e3 本轮仅返导航空壳，故正文优先引用作者动态，不把详情 HTTP 200 写成完整可读。
- [昆仑芯实习面经](https://www.nowcoder.com/discuss/738696660653551616)：搜索正文含 GPU 内存层次、GEMM、bank conflict。覆盖 C07 后两层；原题不含前两层图像预处理/分析流程。

## 搜索索引存证

- [宇树嵌入式 AI 面经](https://www.nowcoder.com/discuss/938361742734655488)：头比板子硬。搜索索引可读两轮内容，含 INT8/PTQ/QAT、剪枝/蒸馏、ONNX/框架/融合、NPU、计算/带宽/零拷贝、控制资源竞争，以及 C++ 内存/生命周期题。覆盖 C01–C06/C08。原详情在 web 工具中不可读，因此不能称已匿名取回全文。
- [另一宇树嵌入式面经](https://www.nowcoder.com/discuss/919881358401372160)：索引内容与前帖高度相似且均推广同一专栏，详情仅导航空壳。不能据此再加独立频次；不采用其参考答案。
- [CUDA 面经](https://www.nowcoder.com/feed/main/detail/d8c2f7acc55745ea8caa24257d8da1c9)：寄了的秋招侠很靠谱，2023-09-01；索引包含 float4、bank conflict、occupancy 等。C07 只以 float4 读取与 bank conflict 为原题锚点，“未提速的诊断”按推断展开。

索引存在不等于完整网页归档；本文保存题目主题与覆盖范围，不能替代外部快照。当前不将多个营销相似帖汇总成 🔥×N。

## 未找回原源

- C13：题单记为“智元中断/启动七连”，但原 URL/作者未留。全链按〔推断〕练习保留，不能宣称为可核实智元实录。
- C07：预处理优化与向量化未提速的完整原链未找回，仅后两层有原始问题证据；其余按推断。

## 原题短摘录与逐层映射

以下记录均于2026-10-26核对；原发布日期未能确认的明确写未知，不能用抓取日期冒充发帖日期。短摘录只作题目锚点，其余映射为主题转述。

### 宇树索引（938361742734655488）

作者头比板子硬；原帖日期未核实（检索相对日期不作为绝对日期）。直接详情未取回正文，搜索索引返回两轮内容。短摘录：“scale和zero-point分别干什么”“推理负载突然增大”。

- C01：主问INT8映射，追1对称/非对称与粒度，追2掉精度，追3PTQ/QAT；FP8及评估分别由下述Cgxiaoxin补齐。
- C02：主问剪枝类型、追1蒸馏；追2未提速诊断是推断。
- C03：主问部署全流程、追1ONNX、追2框架选型、追3融合；按题单主题重排，非宣称原帖连续次序。
- C04：主问NPU/CPU/GPU差异有索引题；两层展开标推断。
- C05：主问瓶颈区分、追1减少搬运、追2/3摄像头链路零拷贝的细分。
- C06：主问共享计算资源时控制按时，追2多模型调度；追1绑核/优先级为推断。
- C08：volatile/static、结构体对齐、堆栈、malloc、浮点/整数、大小端、线程/进程依次来自一面基础问题。

### Cgxiaoxin 原始复盘

作者Cgxiaoxin；页内更新2026-07-03，单场面试日期未知；GitHub contents API取得全文。短摘录：“C++ 智能指针都有哪些”“模型量化 FP32->FP8”。

- C01追4地瓜FP8；追5安努精度评估。
- C09主问智能指针，追1共享设计，追2异常安全，追3线程进程，按湃特纳第6–9题；追4回调扩展标推断。
- C10主问ROS1/2，追1DDS与追3实现差异，追4Topic/Service/Action，来自地瓜第1–3题；追2QoS选型结合湃特纳第5题主题整理。
- C14追1来自安努第1题及讨论要点，追2时空误差诊断标推断。

### 莱修贤作者动态

作者莱修贤；一面2025-02-26 11:26编辑，二面2025-02-27 19:49。本轮主代理web open读到动态摘要，复审工具访问可能不稳定；不声称取得详情完整存档。短摘录：“了解粘包吗”“机械臂的手眼标定的步骤”。

- C10追4图像Topic/Service：二面主题。
- C11主问组帧/粘包、追1大并发、追2长期通信：二面原题顺序；追3实时控制为推断。
- C12主问union/struct、追1混合成员占用空间：一面原题。
- C14主问手眼步骤：二面原题；与Cgxiaoxin动态标定分层拼接。

### CUDA 两帖

- 寄了的秋招侠很靠谱，2023-09-01：[CUDA面经](https://www.nowcoder.com/feed/main/detail/d8c2f7acc55745ea8caa24257d8da1c9)。短摘录：“float4读写gmem为什么更快”。C07追2以原题为锚，未加速情形为推断；追4bank conflict有题。初查详情为空壳，独立审查本轮成功读到正文，访问存在时段/工具差异。
- 逆袭的哈萨维，2025-04-07编辑：[昆仑芯原帖](https://www.nowcoder.com/discuss/738696660653551616)。短摘录：“GPU内存结构”“bank conflict，有什么解决办法”。对应C07追3/4；独立审查本轮读到正文。

## 官方技术校核

- [TensorRT 量化类型](https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/work-with-quantized-types.html)
- [CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)
- [ROS 2 QoS 设计](https://design.ros2.org/articles/qos.html)
- [Linux workqueue](https://docs.kernel.org/core-api/workqueue.html)
- [OpenCV 标定 API](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)

以上只校核技术，不计面经频次。具体库/内核能力以版本文档为准。
