# coding=utf-8
# 通过昵称搜索用户token_url
# 具体数据见Excel文件 zhihu_users_token_url.xlsx
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

user = []
file = open("C:\\Users\\80693\\Desktop\\User_name.txt")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip().split('\t')
    peoples = client.search(line, search_type='PEOPLE')
    people_five = [p for _, p in zip(range(5), peoples)]
    pp = sorted(peoples, key=lambda x: x.obj.follower_count, reverse=True)
    p = pp[0].obj
    print(p.name.ljust(14), p.id.ljust(40), p.follower_count)
    user.append(p.id)