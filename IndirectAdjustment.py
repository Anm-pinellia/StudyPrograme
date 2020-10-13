import numpy as np


watchH = []
watchS = []
'''
print('输入观测值h1,h2,h3,h4')
print('输入观测值S1,S2,S3,S4')

for i in range(4):
    watchH.append(input('h{}:'.format(i)))
    watchS.append(input('S{}:'.format(i)))
'''

h0 = [61.351,59.615,60.154]
S0 = [1,2,2]
for i in range(len(h0)):
    watchH.append(h0[i])
    watchS.append(S0[i])
H = np.array(watchH)
S = np.array(watchS)
print('观测值角度为:\n',H)
print('观测值距离为:\n',S)
print('观测值的内角和为:{}'.format(np.sum(H)))
NumArray = len(S)
UnitWeight = np.zeros((NumArray,NumArray))
row,col = np.diag_indices_from(UnitWeight)
UnitWeight[row,col] = np.array(watchS)
print('单位权矩阵为:\n',UnitWeight)
P = UnitWeight

'''
观测值 + 误差值 = 参数值，       【注】设置的参数值绝对准确
本次设计中以三角形的三个角度为观测值，其误差方程为:
v1 = X1 - L1
v2 = X2 - L2
v3 = -X1 - X2 - L3 + 180
引入未知参数的近似值X = X0 + x
'''
B1 = [1,0]
B2 = [0,1]
B3 = [-1,-1]
B = np.array([B1,B2,B3])

#设置近似值,此例中设置的四舍五入round()方法
X0 = []
for eachnum in h0[:2]:
    X0.append(round(eachnum))
X0yuan = X0.copy()
X0.append(180-X0[0]-X0[1])
X00 = np.array(X0)

#至此，系数矩阵B、常数项矩阵l、单位权矩阵全部获得了P、为了矩阵计算方便，以numpy进行计算
l = -1*(H - X00)

# 求解法方程，根据固定公式，x = (Bt*P*B)-1 * Bt*P*l， 计算出参数误差x
Bt = B.T
temp1 = np.linalg.inv(np.dot(np.dot(Bt,P),B))
x = np.dot(np.dot(np.dot(temp1,Bt),P),l)
#print(x)

#参数平差值,参数平差值X = 参数误差x + 测量参数近似值X0（本例中为X0yuan）
Xping = np.array(X0yuan)+x
#print(Xping)

#观测量的平差值
V = np.dot(B,x) - l
H = H + V

print('观测量平差值为:\n',H)





