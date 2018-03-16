# gift-to-you-ExpertSystem
A course project of SJTU EE397

### 综述

围绕**基于可信度的不确定推理方法**展开，在 Python3环境下搭建了专家系统应用程序，该程序可访问、添加本地 MYSQL数据库，最终实现了具有挑选礼物功能的专家系统。另外 基于 HTML 和 JavaScript 实现了**基于 Web的不确定性推理专家系统**。

### 可信度方法和C-F模型

IF *E*  THEN *H*  (CF(*H*, *E*)) 

CF(*H*, *E*)为可信度因子，当结论不确定时，有合成算法。

<img src="https://raw.githubusercontent.com/summmeer/gift-to-you-ExpertSystem/master/pic_for_md/formula.PNG" width="50%" height="50%">

### 实现

- 界面：wxPython（程序入口：GUI.py）

<img src="https://raw.githubusercontent.com/summmeer/gift-to-you-ExpertSystem/master/pic_for_md/show.png" height="50%" width="50%">
- 数据库：MySQL（首次运行 Database.py 写入规则和对应的置信度，之后的步骤直接对该表进行访问，不需要重新写入规则）

- 推理机：置信度计算

### 不足

- 置信度不足以客观精准地描述知识内容
- 是礼物的种类不够丰富
- 该**专家系统**虽有部分趣味性和实用性，但还是显得笨拙、过时，算法也比较简单

### 网页

[https://summmeer.github.io/gift_to_you_expertSystem](https://summmeer.github.io/gift_to_you_expertSystem)
