---
trigger: model_decision
description: 文档与验收归档技能：涉及文档结构约束、文档更新、测试验证、归档/历史记录、退出与结项流程时使用，并要求遵守项目目录规范与git提交规则。
---

# 文档与验收归档（Docs）

## 概览
保证文档与代码同步、验证流程可追踪、历史记录可恢复。

## 工作流（按顺序执行）
1. 启动读取顺序（缺失则进入降级模式）：
   - `docs/00_project_index.md`
   - `docs/guide/conventions.md`（若存在）
   - `docs/dev_status/active_task.md`
2. 文档架构约束（必须遵守）：
   - 需求工作区：`spec/`（阶段性需求与计划）
   - 模板库：参考本技能披露的模板要点（见 `references/docs-procedures.md`）
   - 待办：`docs/dev_status/todo.md`（倒序）
   - 历史：`docs/dev_status/history_log.md`（倒序）
   - 规范指南：`docs/guide/`
   - 问题追踪：`docs/issues/`
   - 知识库：`docs/product/`、`docs/tech/`、`docs/adr/`
3. 阶段性完成后归档：将 `spec/` 中阶段性成果整理到 `docs/` 对应位置（产品需求、技术设计、运行指南），并在 `docs/00_project_index.md` 中维护索引。
4. 质量控制与验证（必须执行）：
   - 正式测试放 `tests/`，临时验证脚本放 `scripts/scratch/`。
   - 测试命令以 `docs/guide/testing.md` 或 `docs/guide/development.md` 为准。
   - 未运行测试：UNVERIFIED；失败：BROKEN（含修复计划）；通过：VERIFIED（附命令与关键输出摘要）。
5. Git 提交流程：未获用户同意不得提交；若环境不支持 git，输出中文 commit message + 建议命令序列 + 变更文件清单。

## 降级模式与安全
- 无法读取文件必须说明“当前无法访问”；列出需要用户补充的文件清单；提供最小可行建议并标注假设与风险。
- 不记录、不输出真实密钥/Token/私钥/生产数据；示例使用占位符。

## 资源
- 细节流程与模板披露：`references/docs-procedures.md`