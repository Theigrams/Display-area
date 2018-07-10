# coding: utf-8
# 搜集用户信息
from __future__ import unicode_literals, print_function

import os
import pandas as pd
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


info = ['昵称', '关注者', '得赞', '获得感谢', '被收藏', '回答', '文章', '提问', '关注了', '关注问题',
        '性别', 'location', 'business', 'company', 'job', 'major', 'school']
num = len(user_id)
Info = []
for i, peo in zip(range(num), user_id):
    p = client.people(pid=peo)
    data = []
    data.append(p.name)
    data.append(p.follower_count)
    data.append(p.voteup_count)
    data.append(p.thanked_count)
    data.append(p.collected_count)
    data.append(p.answer_count)
    data.append(p.article_count)
    data.append(p.question_count)
    data.append(p.following_count)
    data.append(p.following_question_count)
    data.append(p.gender)
    if p.locations:
        data.append(p.locations[0].name)
    else:
        data.append(' ')
    if p.business:
        data.append(p.business.name)
    else:
        data.append(' ')

    if not p.employments:
        data.append(' ')
        data.append(' ')
    else:
        if 'company' in p.employments[0]:
            data.append(p.employments[0].company.name)
        else:
            data.append(' ')
        if 'job' in p.employments[0]:
            data.append(p.employments[0].job.name)
        else:
            data.append(' ')

    if not p.educations:
        data.append(' ')
        data.append(' ')
    else:
        if 'major' in p.educations[0]:
            data.append(p.educations[0].major.name)
        else:
            data.append(' ')
        if 'school' in p.educations[0]:
            data.append(p.educations[0].school.name)
        else:
            data.append(' ')
    Info.append(data)


data_df = pd.DataFrame(Info)
data_df.columns = info
writer = pd.ExcelWriter('C:\\Users\\80693\\Desktop\\Info_Excel.xlsx')
data_df.to_excel(writer, 'page_1', float_format='%.5f')
writer.save()
