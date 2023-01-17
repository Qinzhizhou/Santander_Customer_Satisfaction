# Santander_Customer_Satisfaction
The kaggle competition solution for predicting if a customer is satisfied or dissatisfied with their banking experience.

## 目前得分：0.82

## 已完成工作：
### 数据集的EDA

### 预处理：
离散化年龄
对数化：连续型数据：var38,imp和saldo 非唯一值特征
标准化

### feature E：
构建新向量：
1.  构建新特征，表示每行样本中143个特征取值为0或者非0的出现次数
2. 构造新特征，表示每行样本对于每一种关键词前缀的特征取值为0或非0的出现次数
3. col特征中每一种为一值的情况下feature特征的均值，并令其为新特征

特征选择: 
1. 删除与目标变量TARGET 低相关的特征
2. 彼此之间高相关的特征

响应编码:解决稀疏化

建模：LR,DT,RF,XGboost

## 未完成工作：
1.独热编码有问题
2.查阅融合模型方案
3. 非平衡取样是否有影响
