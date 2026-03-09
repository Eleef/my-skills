# 迁移指南

本指南将告知你在审阅拆分输出后，需要将哪些内容移动到何处。

## 1. 移入你的规则层 (Rules Layer)
使用此文件作为轻量级的持久化规则核心：
- `rules/DOCOPS_RULES.md`

建议处理方式：
- 将内容合并到你的项目级常驻规则中
- 保持简短；不要将完整的操作流程或模板引用合并到规则层中

## 2. 移入你的正式技能目录 (Formal Skills Directory)
按原样移动这两个文件夹：
- `skills/docops-mode/`
- `skills/doc-template-router/`

原因：
- `docops-mode` 是工作流编排器
- `doc-template-router` 是路由 / 检查清单 / 结构化草案工具

## 3. 将这些参考文件与技能捆绑在一起
### `docops-mode`
- `references/bootstrap_and_states.md`
- `references/implementation_bridge.md`

### `doc-template-router`
- `references/routing_table.md`
- `references/checklists.md`
- `references/template_notes.md`
- `references/structural_templates_platform.md`
- `references/structural_templates_app_core.md`
- `references/structural_templates_app_contracts.md`
- `references/structural_templates_status_and_records.md`

不要将这些文件合并到规则中。它们是技能资源。

## 4. 迁移后的首批测试提示词 (Prompts)
从 `test_prompts.md` 中开始测试以下内容：

### 测试 `docops-mode`
1. 仓库文档重构
2. 多步骤功能文档编写
3. 从规范 (Spec) 到实现的桥接

预期行为：
- 识别多步骤工作流
- 在需要时澄清范围
- 使规范/文档/代码/验证之间的桥接可见
- 在相关时提到开发状态或关闭处理

### 测试 `doc-template-router`
1. 首先选择模板家族
2. 标准路由
3. 微型编辑 vs 结构化编辑

预期行为：
- 清晰地选择一条路由
- 区分标准 (Standards) vs 决策记录 (ADR) vs 词典 (Dictionary) vs 功能 (Feature)
- 对微型编辑使用检查清单
- 仅在需要时使用完整的结构化模板骨架

## 5. 首批不建议测试的内容
避免从微小的一步式提示词开始，例如：
- 简单的文件读取
- 通用概念解释
- 无文档影响的纯代码变更

这些通常不应触发任何一个技能。

## 6. 迁移成功的标准
迁移状况良好，如果：
- 规则保持轻量
- `docops-mode` 处理工作流以及从规范到实现的桥接
- `doc-template-router` 处理位置和模板路由
- 标准不再与 ADR 或词典文档混淆
- 验收标准影响验证，而不仅仅是作为纯文本存在

## 7. 建议的后续步骤
移动文件后，运行 `test_prompts.md` 中的手动提示词并记录：
- 触发了哪个技能
- 提示词是否存在触发不足或过度触发的情况
- 所选路由是否自然

只有在触发行为感觉不对时，才进行最后一轮的描述微调。
