---
title: 流程控制
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, flow-control, if, while, for]
updated: 2026-04-16
---

## 目录
- [概念](#概念)
- [语法规则](#语法规则)
- [代码示例](#代码示例)
- [易错点](#易错点)
- [小练习](#小练习)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 概念
- 流程控制决定代码按什么条件执行、重复执行以及何时提前退出。
- 写流程控制时，关键不是“语法会不会写”，而是条件边界是否清晰、循环是否可终止。
- `for-else` 与 `while-else` 是 Python 里常被忽略但非常实用的结构。

## 语法规则
- `if/elif/else` 按顺序匹配第一个满足条件的分支。
- `while` 适合“满足条件就继续”的场景，循环变量必须能趋近结束条件。
- `for` 适合遍历可迭代对象，配合 `range()` 能完成绝大多数计数循环。
- `break` 会提前结束循环，`continue` 会跳过本轮剩余逻辑，`else` 只会在循环未被 `break` 打断时执行。

## 代码示例
### 示例 1：条件分支

```python hl_lines="3 5 7"
response_time = 320

if response_time < 200:
    level = "fast"
elif response_time < 500:
    level = "acceptable"
else:
    level = "slow"

print(level)
```


### 示例 2：`for` + `range`

```python hl_lines="2 3"
total = 0
for number in range(1, 6):
    total += number
print(total)
```


### 示例 3：`for-else`

```python hl_lines="3 6 8"
users = ["alice", "bob", "charlie"]

for user in users:
    if user == "dora":
        print("found")
        break
else:
    print("not found")
```

## 易错点
- `while True` 写得很顺手，但如果没有清晰退出条件，就很容易写出死循环。
- 在遍历列表时直接删除元素，会改变索引和长度，常导致漏处理数据。
- 很多人把 `for-else` 误解成“循环结束后总会执行 else”，其实只有没有被 `break` 打断时才会进 else。

## 小练习
1. 遍历 1 到 20，打印所有能被 3 整除但不能被 2 整除的数字。
2. 写一个 `while` 循环，把字符串列表中长度小于 3 的元素过滤掉。
3. 使用 `for-else` 判断某个用户名是否存在于用户列表里。

完成后再对照“参考答案”和“Self-Check”复盘。

## Self-Check
### 概念题
1. `for` 和 `while` 的选择标准是什么？
2. `for-else` 的 `else` 到底在什么时候执行？
3. 为什么流程控制里要特别关注“终止条件”？

### 编程题
1. 怎样用 `range()` 遍历 0 到 8 的偶数？
2. 如何在遍历列表时安全过滤元素？

### 实战场景
1. 你在轮询接口状态，直到任务完成或超时，该用什么流程结构更合适？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
当你知道要遍历一个集合或固定次数时优先用 `for`；当循环是否继续取决于动态条件时用 `while` 更自然。
讲解回看: [语法规则](#语法规则)

### 概念题 2
只有循环正常结束且没有触发 `break` 时才执行；如果提前 `break`，`else` 不会运行。
讲解回看: [代码示例](#代码示例)

### 概念题 3
因为边界不清晰时最常见的问题就是死循环、漏处理和分支覆盖不完整，这些都会直接影响测试脚本稳定性。
讲解回看: [概念](#概念)

### 编程题 1
使用 `range(0, 10, 2)`。起点是 0，终点不包含 10，步长为 2。
讲解回看: [语法规则](#语法规则)

### 编程题 2
优先创建新列表，例如列表推导式或结果列表累加，避免在遍历原列表时直接删除元素。
讲解回看: [易错点](#易错点)

### 实战场景 1
通常用 `while`，因为是否继续轮询取决于接口返回状态和超时阈值。循环里应显式维护重试次数或截止时间。
讲解回看: [概念](#概念)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
