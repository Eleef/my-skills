# 规范到实现的桥接 (Spec-to-Implementation Bridge)

当任务从已明确的需求转向实际实施时，请使用此笔记。

## 实现入口检查清单 (Implementation entry checklist)
在编码前，请明确以下内容：
- 正在解决的需求
- 主要规范文档
- 适用的标准 / ADR / 平台约束
- 预期变更的代码区域
- 预期变更的文档区域
- 待验证的验收标准
- 验证计划

## 映射规则 (Mapping rules)
### 如果变更是功能级 (Feature-level) 的
- 功能文档承载目标、范围、UX 和验收标准。
- 词典 (Dictionary) 文档承载 API/数据/UI 契约。
- 代码实现其中定义的行为。

### 如果变更是契约级 (Contract-level) 的
- 先更新权威规范，或与代码原子性地同步更新。
- 应用拥有的契约使用 `docs/apps/<app>/dictionary/**`。
- 平台拥有的共享契约使用 `docs/platform/<component>/specs/**`。
- 功能文档应引用已变更的契约，而非重复陈述。

### 如果变更是跨应用可重用的
- 在 `docs/platform/standards/**` 下添加或更新标准文档。
- 根据需要从功能、ADR 或实现笔记中链接该标准。

### 如果变更是架构级 (Architectural) 的
- 当权衡超出一个局部补丁的影响范围时，在 ADR 中记录决策。

## 验证映射 (Verification mapping)
- 每个有意义的验收标准都应有一个验证步骤。
- 如果不存在可运行的命令，请定义一个冒烟测试或可观察的结果。
- 如果验证失败，请勿声称已完成；标注为 `BROKEN` 并记录差距。

## 收尾映射 (Closure mapping)
完成后，确保最终状态反映在：
- 实现或代码摘要中
- 已变更的文档中
- 验证状态中
- 相关的 `dev_status/**` 文件中
- 问题/故障排除/ADR 条目中（如果工作产生了持久的运维知识）
