# coding=utf-8
# 爬取用户相关度 并储存用户相关矩阵
import numpy as np
import pandas as pd
from __future__ import unicode_literals, print_function

import os

from zhihu_oauth import ZhihuClient


TOKEN_FILE = 'token.pkl'
client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)

user_id = []
file = open("C:\\Users\\80693\\Desktop\\User_id.txt")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip().split('\t')
    user_id.append(line[0])


user_name = []
file = open("C:\\Users\\80693\\Desktop\\User_name.txt")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip().split('\t')
    user_name.append(line[0])

num = len(user_id)
link = np.zeros([num, num])
for i, peo in zip(range(num), user_id):
    p = client.people(pid=peo)
    for follow in p.followings:
        if follow.id in user_id:
            link[i][user_id.index(follow.id)] = 1


data_df = pd.DataFrame(link)
data_df.columns = user_name
data_df.index = user_name
writer = pd.ExcelWriter('C:\\Users\\80693\\Desktop\\Link_mat.xlsx')
data_df.to_excel(writer, 'page_1', float_format='%.5f')
writer.save()

data_df.to_csv('C:\\Users\\80693\\Desktop\\link.csv',
               index=False, header=False)
