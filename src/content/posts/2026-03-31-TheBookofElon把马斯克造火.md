---
title: "《The Book of Elon》：把马斯克造火箭的“算法”，硬塞进大模型堆栈"
description: "曾把纳瓦尔（Naval Ravikant）的推文整理成神作《纳瓦尔宝典》的作者 Eric Jorgenson，最近又扔出了一颗重磅炸弹——《The Book of Elon: A Guide to Purpose and Success》（"
pubDate: 2026-03-31
category: "ai-engineering"
tags: ["RAG", "Agent", "行业观察"]
draft: false
---

<br><br>


### 这不是硅谷鸡汤，这是工程师的“原教旨”

曾把纳瓦尔（Naval Ravikant）的推文整理成神作《纳瓦尔宝典》的作者 Eric Jorgenson，最近又扔出了一颗重磅炸弹——《The Book of Elon: A Guide to Purpose and Success》（马斯克之道）。

这书花了五年时间，从马斯克数百万字的访谈和推文中提炼而成。如果你把它当成机场书店里卖的“成功学鸡汤”，那你就彻底错了。
在《Agent 降临派》看来，这本书的核心，尤其是马斯克反复强调的**“The Algorithm（算法）”**，简直就是当前打造最强本地 AI Agent 的终极操作手册。

### Agent 时代的“第一性原理”

现在的 AI 圈有一种极度恶臭的趋势：**做加法**。
为了让大模型表现得更聪明，开发者们在拼命地堆叠外围架构——给它挂上几百 GB 的 RAG（检索增强生成）向量库，写几千 Token 长的“系统提示词（System Prompt）”，设计七八层嵌套的思维链。

结果呢？就像猎鹰一号早期的火箭一样，系统越臃肿，崩溃得越快（参考之前的 ARC-AGI-3 惨案，模型在庞大的上下文里直接患上了“精神分裂”）。

马斯克在星舰和特斯拉产线上总结出的**“五步算法（The Algorithm）”**，是对这种臃肿风气的降维打击：

1. **质疑每一项要求（Question the requirement）**：大模型真的需要知道所有历史背景才能写这行代码吗？如果不是，删掉它。
2. **尽一切可能删除零件（Delete any part or process you can）**：马斯克说，如果你没有在后续被迫加回至少 10% 的零件，说明你删得还不够狠。放到 Agent 身上就是：删掉所有冗余的 Prompt 和冗余的插件，直到它报错为止。
3. **简化与优化（Simplify and optimize）**：这也是最常犯的错误——人们总是倾向于去优化一个原本根本就不该存在的流程。
4. **加速周期（Accelerate cycle time）**：别管你的 Workflow 有多完美，让 Agent 用最快的速度跑完第一个闭环，把代码或结果吐出来。
5. **自动化（Automate）**：当前四步被极致压缩后，再交给机器去自动循环。

### 降临派生存法则：极度删减

为什么当前最聪明的开发者都在把 Agent 做小、做轻？（比如 Claude Code 的后台内存清理机制 AutoDream）。
因为在这个算力和 Token 变得像水和电一样便宜的时代，真正的核心壁垒不再是你能给机器喂多少数据，而是你敢于**删掉多少噪音**。

《The Book of Elon》给所有 AI 开发者上了最冷酷的一课：**工程的极致不是无所不包，而是无可删减。**

不要再去迷信几万字的“终极提示词”了。拿起你的赛博手术刀，砍掉那些没用的堆栈，把马斯克的这套“极简算法”硬塞进你的本地 Agent 里。
那是你在接下来的 AI 算力军备竞赛中，唯一能跑赢巨头的底牌。

<br><br>
