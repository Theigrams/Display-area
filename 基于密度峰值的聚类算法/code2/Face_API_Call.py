# -*- coding: utf-8 -*-
# 调用Face++ API计算fig文件夹下图片的相似度矩阵
import urllib2
import urllib
import time
import numpy as np
http_url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
key = "MSEuYIibv2ldXKRoNTq61tNmqlT4POaN"
secret = "vlhOUyZ0PKNJLIJYWX9yKUOHj47Rc5XF"


def fun(i, j):
    filepath1 = r"C:\Users\80693\Desktop\fig\%s.jpg" % (i + 1)
    filepath2 = r"C:\Users\80693\Desktop\fig\%s.jpg" % (j + 1)
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' %
                'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' %
                'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr1 = open(filepath1, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' %
                'image_file1')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr1.read())
    fr1.close()
    data.append('--%s' % boundary)
    fr2 = open(filepath2, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' %
                'image_file2')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr2.read())
    fr2.close()
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header(
        'Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        # print qrcont
        return eval(qrcont)["confidence"]
    except urllib2.HTTPError as e:
        print e.read()
        print "第%s张图与第j张图中的相似度未算出来" % (i + 1, j + 1)


N = 9
A = np.ones((N, N)) * 100
for i in range(N):
    for j in range(i + 1, N):
        A[i][j] = A[j][i] = fun(i, j)
        time.sleep(3)
