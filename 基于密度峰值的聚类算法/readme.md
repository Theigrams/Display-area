## 报告说明
本项目源于数学软件课的一次大作业，我们研读论文《clustering by fast search and find of density peaks》，然后进行仿真实验，比较其与其他聚类算法的优劣，并应用到人脸分类上。

## 文档说明

### code1

`code1 `文件夹中的 `txt` 文件为数据集，两个MATLAB程序分别代表两个聚类算法，使用方法如下：

- `Clustering by density peaks.m` ：

   需要测试数据集"D31.txt"时，需要将程序第6行改为   
   ```matlab
   load('D31.txt');
   ```
   将第7行改为：

   ```matlab
   P=D31;
   ```

   然后就可以运行，其他类似。

- `k_mean_test.m` ：

   需要测试数据集"D31.txt"时，需要将程序第3行改为   

   ```matlab
   load('D31.txt');  
   ```

   将第5行改为：

   ```matlab
   P=D31;
   ```

   再手动将第4行将N设定为聚类的个数

   然后即可运行

### code2

- `Face_API_Call.py`  为调用API计算图片相似度矩阵，需要在第13,14行更改文件目录，并且程序运行时间较长，期间可能某些图片之间的相似度计算会出现错误。程序运行完后需要手动将矩阵提取出来。
- `data_transformation.m` 为将相似度矩阵转化为距离信息的程序，运行完毕后将会生成一个 `data1.dat` 文件
- `cluster.m`  载入 `data1.dat` 数据并进行聚类
