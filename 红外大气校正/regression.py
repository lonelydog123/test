import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 通过read_csv来读取我们的目的数据集
new_adv_data = pd.read_csv("C:/Users/user/Desktop/model_1.csv")
# 利用sklearn里面的包来对数据集进行划分，以此来创建训练集和测试集
# train_size表示训练集所占总数据集的比例
X_train, X_test, Y_train, Y_test = train_test_split(new_adv_data.iloc[:, :2], new_adv_data.T0, train_size=.80)

model = LinearRegression()
model.fit(X_train, Y_train)
a = model.intercept_  # 截距
b = model.coef_  # 回归系数
print("Best fitting line:intercept", a, ",Regression coefficient：", b)
score = model.score(X_test, Y_test)
print(score)