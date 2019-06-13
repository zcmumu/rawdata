# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import xlrd
# with open(r"C:\Users\320062702\Desktop\raw_data\session.log", "r") as f:    #打开文件
#    data = f.read()   #读取文件
#    print(data)

'''
plt.figure()

y_raw = [int(l.split()[28]) for l in open(r"E:\program\data.txt")]  # 读取文件中甲醛数值，转化为数值型
x_raw = [(l.split()[1]) for l in open(r"E:\program\data.txt")]

# plt.plot(x,y)     画图
# plt.show()


sum = 0
x = []
y = []
for i in range(len(y_raw) - 12 * 10):  # 取前十分钟均值
    for s in range(i, i + 120):
        sum += y_raw[s]
    y.append(int(sum / 120))
    x.append(i)
    sum = 0

plt.plot(x,y)
plt.show()

print(x)


'''
# print(len(y_raw))      #数组长度

data = xlrd.open_workbook(r'D:\桌面文件\工作\ao甲醛测试6-10.xlsx')
print(data.sheet_names())
table = data.sheets()[1]
print(table.nrows)
