import numpy as np


watchH = []
watchS = []

inputflag = input('需要自己定义系数矩阵和权阵吗?(yes/no)\n')
if inputflag == 'no':
    h0 = [1.003,0.501,0.503,0.505]
    S0 = [0.5,1,1,0.5]
    b = [[1, 0], [-1, 1], [0, 1], [1, 0]]
    l0 = [0,1,0,2]
    x0 = [2.003, 2.503]
else:
    b = []
    h0 = []
    S0 = []
    l0 = []
    x0 = []

    n = int(input('请输入观测数据个数:'))
    for i in range(n):
        h0.append(float(input('请输入观测值数据{}:'.format(i+1))))

    n0 = int(input('请输入参数个数:'))
    for i in range(n):
        temp = []
        for j in range(n0):
            temp.append(float(input('请输入{}.{}位置的值'.format(i + 1, j + 1))))
        b.append(temp)
    print('系数矩阵列表为:\n',b)

    for i in range(n):
        S0.append(float(input('请输入权阵数据{}:'.format(i+1))))

    for i in range(n):
        l0.append(float(input('请输入自由项阵数{}:'.format(i+1))))

    for i in range(n):
        x0.append(float(input('请输入参数近似值{}:'.format(i+1))))


for i in range(len(S0)):
    watchH.append(h0[i])
    watchS.append(S0[i])
L0 = np.array(watchH)                #L为观测值
P0 = np.array(watchS)                #P0为权重
print('观测值角度为:\n',L0)
print('观测值距离为:\n',P0)
print('观测值的内角和为:{}'.format(np.sum(L0)))

P = np.zeros((len(P0),len(P0)))
row,col = np.diag_indices_from(P)
P[row, col] = np.array(P0)          #P为权重矩阵

X0 = np.array(x0)                #参数的近似值X0
B = np.array(b)
print('B is ',B)
L = np.array(h0)
L = np.expand_dims(L,axis=0).T
#l = L - (np.dot(B,X0))                #l为自由项阵，B为系数阵
l = np.array(l0)
l = np.expand_dims(l,axis=0).T
print('l is ',l)
print('P is ',P)



x = np.dot(np.dot(np.dot(np.linalg.inv(np.dot(np.dot(B.T,P),B)),B.T),P),l)          #x为参数的改正数
V = np.dot(B,x)-l
print('V is',V)
print('L is',L)

LAdValue = L+V*0.001
XadValue = X0+x.T*0.001

print('参数改正数 x is \n',x)
print('观测值的平差值为\n',LAdValue)
print('参数值的平差值为\n',XadValue)









