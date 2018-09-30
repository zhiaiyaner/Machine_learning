import numpy as  np
import matplotlib.pyplot as plt
import txt_3 as  t1
Xlist=[]
Ylist=[]
Xlist,Ylist=t1.txt()
print('Xlist=',Xlist)
print('Ylist=',Ylist)

b=float((np.random.random()*20)-10)
k=float((np.random.random()*20)-10)
print(b,k)

#梯度下降
sum_x=sum(Xlist)
sum_y=sum(Ylist)
L=len(Ylist)
alpha=0.01
last_sum=float(5)

n_1=[]
n_2=[]
for i in range(1,10000):
    dk=0 #偏导k斜率
    db=0
    for j in range(0,L):
        dk=dk+(Xlist[j]*(k*Xlist[j]+b-Ylist[j]))
        db=db+(k*Xlist[j]+b-Ylist[j])
    if(np.fabs(last_sum-db)<(1e-6)):
        break


    n_1.append(i)
    n_2.append(sum_y-db)

    last_sum=db
    dk=dk/L #最后的偏导
    db=db/L
    k=k-alpha*dk
   # n_1.append(k)
    b=b-alpha*db
    #n_2.append(b)
    print('i=',i),print('\t'),print('k=',k),print('\t'),print('b=',b)
plt.figure(1)
plt.scatter(Xlist,Ylist)
x_1=np.linspace(0,30,30)
y_1=k*x_1+b
plt.plot(x_1,y_1,c='r')
print(n_1)
print(n_2)

plt.figure(2)
plt.scatter(n_1,n_2)
plt.show()
