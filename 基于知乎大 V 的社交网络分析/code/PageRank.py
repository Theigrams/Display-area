# coding=utf-8
# 载入CSV文件 计算PageRank值
import numpy as np
import pandas as pd
link = pd.read_csv('C:\\Users\\80693\\Desktop\\link.csv', header=None)
np.array(link)
A = link + 0.000000001
A = A.T
a = np.sum(A, 0)
A = A / a
alpha = 0.85
B = np.ones([a.size, 1]) / a.size
E = (1 - alpha) * B

for i in range(1000):
    B = alpha * np.dot(A, B) + E
print(B)

user_name = []
file = open("C:\\Users\\80693\\Desktop\\User_name.txt")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip().split('\t')
    user_name.append(line[0])

data_pr = pd.DataFrame(B)
data_pr.columns = ['PR Vaule']
data_pr.index = user_name
writer = pd.ExcelWriter('C:\\Users\\80693\\Desktop\\PR_Vaule.xlsx')
data_pr.to_excel(writer, 'page_1', float_format='%.5f')
writer.save()
