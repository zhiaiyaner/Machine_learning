import  os
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


f=open('ex1data1.txt','r')
sourceInLine=f.readlines() #每一行每一行的读取文本，并且一次性读取所有文本，并不且可以for循环里面按行操作
dataset=[]
def txt():
    for line in sourceInLine:
        temp1=line.strip('\n') #strip()为剔除符号，把()里面标注的字符删除掉
        temp2=temp1.split(',') #split（）按照括号里面的符号分割字符串，也就是切片，切成几块就是几块
        a=0
        b=0
        for i in range(0,2):
            if i==0:
                a=temp2[0] #也是一个list，所以可以这样操作
            if i==1:
                b=temp2[1]
        a=float(a)
        b=float(b)
        dataset.append([a,b])#按照行导入到list中
    a=dataset
    #print('a=',a)
    x=[]
    y=[]
    for i in range(len(a)):
        x.append(a[i][0])
        y.append(a[i][1])
    #print('x=',x)
    #print('y=',y)
    #plt.scatter(x,y)
   # plt.show()
    return x,y

