# DocOps 拆分产物

这个目录保存了把原始 DocOps 工作流标准拆分后的可落地版本，分为三层：

- `rules/`：轻量、常驻的全局规则
- `skills/docops-mode/`：负责工作流推进、状态切换、bootstrap、spec 到实现桥接、handoff
- `skills/doc-template-router/`：负责模板路由、标准文档归类、checklist 校验、结构化起草

## 目标
- 为 agent 提供一套可执行的 DocOps 工作模型，让仓库文档成为交付流程的一部分，而不是仅用于事后记录。
- 把常驻规则保持在最小规模，把较重的流程控制和文档起草能力放进按需触发的 skills，降低默认上下文负担。
- 明确区分“阶段中的活跃工作区”和“已发布知识库”：
  - `spec/**` 用于需求澄清、验收说明、实现笔记、验证计划等高频演化中的材料
  - `docs/**` 用于已发布、可引用、可作为依据的长期文档和权威文档
- 让文档路由变得显式，agent 可以更快判断当前请求应该落到 feature、dictionary、platform standards、ADR、issue 还是 dev_status。
- 在文档逐渐增多时控制上下文膨胀：
  - 先读取 YAML Front Matter
  - 再根据 `kind` 采用局部读取规则，而不是默认整篇读取
  - 对 history、todo、status 这类日志文档按局部窗口读取，而不是整篇扫描
- 维护 SSOT 边界，让契约留在 authority doc 中，feature 文档通过链接引用，而不是复制 schema 细节。
- 提升开发过程中的交接质量，让 `docs/dev_status/**`、git checkpoint、已发布文档在关键节点保持一致。
- 支持从澄清到实现再到归档的阶段化流转：
  - 在 `spec/**` 中澄清、草拟、迭代
  - 在 `docs/**` 中发布权威内容或长期知识
  - 阶段结束后归档、收缩或移除只在本阶段有效的工作材料

## 建议用法
- 审阅后，把 `rules/DOCOPS_RULES.md` 合并进项目的常驻规则层。
- 把两个 skills 作为按需触发的工作流组件使用，而不是塞进 always-on 上下文。
- 默认把 `spec/**` 当作阶段中的活跃工作区，把稳定的 authority 或长期知识发布到 `docs/**`。
- 使用 YAML Front Matter 和按 `kind` 的正文读写规则，让 agent 在读正文前先完成 triage。
- 仓库文档很多时，可选用 `skills/docops-mode/scripts/metadata_index.py` 先批量读取受限 front matter，再决定是否展开正文读取。
- 模板、路由、checklist 的演进尽量放在 skill references 中，不要继续把规则层写胖。
- 迁移前先用 `test_prompts.md` 做手工触发测试。
- 迁移步骤和首轮测试顺序见 `MIGRATION_GUIDE.md`。

## 为什么这样拆
- 稳定约束应放在 `rules`。
- 多步骤工作流应放在 workflow skill。
- 模板路由、checklist、结构化起草应放在 template skill。

## 后续演进方向
- 当前先保持这个 skill 拆分，不继续细拆。
- 如果未来出现触发重叠或上下文压力，优先按工作流频率拆 `docops-mode`，而不是按文档类型拆。
- 可能的方向：
  - 高频中段流程继续留在 `docops-mode`，例如 docs sync、dev_status 迭代、spec-to-implementation bridge、template delegation
  - 低频边界动作以后再拆成独立 helper，例如 kickoff / planning start、pause / completion / archive
