## 报告说明
本项目来源于随机过程课的一次大作业，用Python爬取知乎用户数据，然后找出大V之间的社交关系，对该社交网络进行分析。

## 文件说明

- `Info_search.py`
- `Link_search.py`
- `Token_url_search.py`
这三个都是爬取数据的程序

`PR.m` 和 `PageRank.py` 是分别用MATLAB和Python算PageRank的程序

`Info_2018_5_26.xlsx` 是具体的知乎用户信息

`Link_mat.xlsx` 是相互关注矩阵，A(i,j)=1代表用户 i 关注了用户 j

(`link.csv` 也是关注矩阵，只是把姓名去掉了，方便程序调用)

`PR_Vaule.xlsx` 是算出来每个用户的PageRank值

`中心性数据统计.xlsx` 储存了每个用户基于不同中心性的值

