---
title: 机器学习入门与模型闭环
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, machine-learning, scikit-learn, evaluation, model]
updated: 2026-04-17
---

## 目录
- [为什么学](#为什么学)
- [学什么](#学什么)
- [怎么用](#怎么用)
- [业界案例](#业界案例)
- [延伸阅读](#延伸阅读)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 为什么学
- 机器学习主题的价值，不只是会调一个库，而是把数据、特征、训练、验证、评估和上线约束连成闭环。
- 测试工程虽然不一定天天训练模型，但越来越多场景要理解分类、回归、聚类、召回率和误报漏报。
- 初学时如果先背算法名词，很容易失去上下文；先抓任务类型和评估方式，后面学任何模型都会快很多。

## 学什么
- 先分清监督学习、无监督学习和简单规则系统的边界，再去看具体算法。
- 一个最小机器学习闭环至少包括“准备数据、拆分训练与验证、建立基线、训练模型、评估结果、解释错误样本”。
- 在工程里，数据质量、特征定义和评价指标往往比模型名字更重要。

## 怎么用
### 示例 1：先用纯 Python 做一次训练 / 测试拆分

```python hl_lines="2 5 8"
samples = [("small", 0), ("medium", 0), ("large", 1), ("xlarge", 1)]
split_index = len(samples) // 2
train = samples[:split_index]
test = samples[split_index:]

print(train, test)
```


### 示例 2：用纯 Python 计算最基础的分类评估指标

```python hl_lines="3 7 10"
truth = [1, 0, 1, 1]
prediction = [1, 0, 0, 1]
tp = sum(1 for expected, actual in zip(truth, prediction) if expected == actual == 1)
fp = sum(1 for expected, actual in zip(truth, prediction) if expected == 0 and actual == 1)
fn = sum(1 for expected, actual in zip(truth, prediction) if expected == 1 and actual == 0)
accuracy = sum(1 for expected, actual in zip(truth, prediction) if expected == actual) / len(truth)
precision = tp / (tp + fp) if tp + fp else 0.0
recall = tp / (tp + fn) if tp + fn else 0.0

print(round(accuracy, 2), round(precision, 2), round(recall, 2))
```


### 示例 3：可选地检测 scikit-learn 是否可用

```python hl_lines="1 4 9"
try:
    from sklearn.neighbors import KNeighborsClassifier
except ImportError:
    print("install scikit-learn before running the full machine-learning workflow")
else:
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit([[1], [2], [10], [11]], [0, 0, 1, 1])
    prediction = model.predict([[3], [12]])
    print(prediction.tolist())
```


落地建议:
- 学每个算法前先问自己三件事：任务类型是什么、输入特征是什么、评价指标是什么。
- 不要一上来就追求复杂模型，先做基线，再看误差来自数据、特征还是模型能力。
- 任何模型结果都要配合错误样本和业务成本解释，不能只看一个分数。

## 业界案例
- 质量平台做缺陷分类时，往往先从规则和简单分类器做基线，再逐步增加特征和模型复杂度。
- 推荐、风控、搜索排序这类业务虽然模型不同，但都离不开数据切分、指标设计和错误分析。
- 真正影响项目成败的，经常不是模型训不出来，而是标签质量、样本分布和上线评估没设计清楚。

## 延伸阅读
- 先学会解释准确率、召回率、精确率、过拟合、数据泄漏，再扩展到更复杂的模型结构。
- 机器学习要和数据分析连起来学，不要把特征工程和清洗过程丢在模型之外。
- 一个模型如果不能解释输入、输出、风险和监控方式，就还不算工程可交付。

## Self-Check
### 概念题
1. 为什么机器学习学习顺序应该是“任务类型 -> 数据拆分 -> 评估方式 -> 算法细节”？
2. 准确率、精确率和召回率分别回答什么问题？
3. 为什么说模型调参不是机器学习工作的全部？

### 编程题
1. 写一个最小训练 / 测试拆分示例，并打印拆分结果。
2. 写一个最小指标计算脚本，输出 accuracy、precision 和 recall。

### 实战场景
1. 你要做一个“是否需要人工复核”的二分类模型，为什么不能只看准确率，还要结合误报和漏报成本一起评估？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为只有先确定任务、数据和评估，算法选择才有意义；不然很容易出现“会调库但不知道结果代表什么”。
讲解回看: [学什么](#学什么)

### 概念题 2
准确率看整体猜对比例，精确率看预测为正时有多少是真的，召回率看真实为正时抓回来了多少。
讲解回看: [怎么用](#怎么用)

### 概念题 3
因为数据质量、标签可靠性、特征设计和上线监控同样决定模型最终是否可用。
讲解回看: [为什么学](#为什么学)

### 编程题 1
即使先不用现成库，也可以先用切片或索引把样本拆成训练集与测试集，先理解闭环再上工具。
讲解回看: [怎么用](#怎么用)

### 编程题 2
按 `tp`、`fp`、`fn` 定义把指标手算一遍，会比直接背 API 更容易真正理解模型评估。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
因为漏报会放过风险样本，误报会增加人工成本，评价指标必须反映真实业务代价。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [scikit-learn 文档](https://scikit-learn.org/stable/documentation.html)
- [NumPy 文档](https://numpy.org/doc/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的机器学习入门、常见算法与实战主题折叠进主线路径专题。

---
[返回 Python 学习总览](../README.md)
