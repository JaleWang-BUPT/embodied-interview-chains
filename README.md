# 具身智能面试追问链 · Embodied Interview Chains

按“主问 → 追问 → 深挖”组织的中文学习题库。七卷共 **81 条链、322 个已答问答节点**，附可运行的手写算法与 PyTorch 示例。

[在线阅读](https://jalewang-bupt.github.io/embodied-interview-chains/) · [生产流程](WORKFLOW.md) · [格式规范](docs/format-spec.md) · [审查记录](research/reviews/)

网页默认折叠：先自己回答，再展开对照，最后合上复述。支持手机浏览；折叠无需 JavaScript，公式排版使用 MathJax CDN，CDN 不可用时仍能阅读公式源文。

## 全卷目录

| 卷 | 内容 | 链 / 节点 | Markdown | 题源与边界 |
|---|---|---:|---|---|
| 一 | VLA 与模仿学习 | 17 / 53 | [正文](volumes/vol1_vla_il.md) | [题源](research/sources-vol1.md) |
| 二 | 强化学习与运动控制 | 16 / 71 | [正文](volumes/vol2_rl_motion.md) | [题源](research/sources-vol2.md) |
| 三 | 数据 · 遥操作 · 真机排障 | 12 / 48 | [正文](volumes/vol3_data_teleop_debug.md) | [题源](research/sources-vol3.md) |
| 四 | 部署 · 系统 · 嵌入式 | 14 / 61 | [正文](volumes/vol4_deployment_systems.md) | [题源](research/sources-vol4.md) |
| 五 | 项目答辩 · 面试攻防 | 11 / 40 | [正文](volumes/vol5_project_defense.md) | [题源](research/sources-vol5.md) |
| 六 | 感知 · 标定 · SLAM | 3 / 18 | [正文](volumes/vol6_perception_slam.md) | [题源](research/sources-vol6.md) |
| 附录 | 手撕与最小测试 | 8 / 31 | [正文](volumes/vol7_coding_appendix.md) | [题源](research/sources-appendix.md) |

本阶段题单已全部成稿，节点数按“主问 + 带答案的编号追问”统计；阅读提示不另计节点。原[题单初稿](research/题单初稿.md)是历史规划，不代表最终频次或证据等级。

## 题源与审查

本库同时包含公开实录主题、整理与推断练习，**不是所有问题都能证明某公司真实考过**：

- 详情正文、作者动态、搜索索引和历史自记分开标注；HTTP 200 不等于正文可读。访问状态记录于核验时点，不保证持续可用。
- 未取得独立原文的历史题单降为推断，不把本仓库自记当第三方快照，不用 prep 站或营销相似帖虚增实录频次。
- 跨场拼接、主题重排、工程扩展逐层说明。除明确引用外，“易错”是编者工程归纳，不代表候选人真实失误。
- 新修内容经独立上下文交叉审查，保留 FAIL 与后续复检。记录包含配置模型及身份核验限度；PASS 只覆盖注明的范围与文件快照，不是面试真实性或真机安全认证。
- 网页审查状态按最新轮次及 SHA-256 自动计算；被审正文、题源或代码变化会使旧 PASS 失效。CI 要求七卷均有当前独立审查 PASS 才部署。

旧卷本轮也重新核查并修正技术结论、撤销未经证实的频次。历史审查文件保留，不覆盖或抹去之前的错误记录。

## 本地检查与渲染

需要 Node.js 20+；题库渲染无 npm 依赖：

```bash
node --test tests/content.test.mjs
node tools/validate.mjs --require-reviewed
node tools/render.mjs
node tools/check-site.mjs
python3 -m http.server 8000 --directory site
```

开发草稿时可不带 `--require-reviewed`，但发布检查会阻断未审或快照不匹配的内容。字数检查忽略 Markdown 强调、代码/数学分隔符和空白，英文逐 Unicode 码点计，保留 LaTeX 命令。

## 可运行手写示例

[标准库实现](examples/handwritten.py)含 softmax、二维互相关、PID、旋转、牛顿迭代、标量 KF、链表、堆与 BFS；[PyTorch 实现](examples/learning.py)含显式 MHA、有效动作 masked MSE、条件 FM、Euler 采样与 PPO actor loss。每个实现的形状、假设和边界见 docstring。

只运行标准库的 13 项测试，无需额外依赖：

```bash
python3 -m unittest discover -s tests -p test_handwritten.py -v
```

完整复现（已在 Python 3.13、PyTorch 2.14.1 CPU 环境验证，25 项 Python 测试无跳过）：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-test.txt --index-url https://download.pytorch.org/whl/cpu
.venv/bin/python -m unittest discover -s tests -v
```

未安装 PyTorch 时，学习部分会明确显示 skipped，不能当作全部通过。CI 安装 CPU 依赖后测试，部署同时依赖内容校验、页面检查和示例测试成功。

这些是学习用最小实现，不是完整训练框架或生产控制器；数值测试不证明机器人稳定性。涉及真机时应遵守硬件规范、低风险台架与现场安全流程。

## 维护

按 [WORKFLOW.md](WORKFLOW.md) 先审题单，再起草、独立审查、渲染和发布。新增来源时立即记录作者/日期（未知则明说）、原题短摘录、访问方式及逐层映射；不要等到源帖失效后再补造证据。

贡献请说明改动范围、证据及验证结果。内容与代码采用 [MIT License](LICENSE)。
