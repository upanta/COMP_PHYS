import numpy as np

n_input=4
n_hidden=3
n_out=2

lambda_h=0.6
lambda_o=1.6

w_ij = np.matrix([[0.5, 0.3, 0.9],
		[0.1, 0.2,0.4],
		[0.3,0.4,0.1],
		[0.2,0.8,0.5]])



w_jl = np.matrix([[0.1,0.4],[0.3,0.2],[0.4,0.7]])

w_jlLIST = [[0.1,0.4],[0.3,0.2],[0.4,0.7]]

x = np.matrix([0.1,0.2,0.3,0.4])
xLIST = [0.1,0.2,0.3,0.4]

def f_hidden(x):
	f =1/(1+np.exp(-lambda_h*x))
	return f

def f_out(x):
	f=1/(1+np.exp(-lambda_o*x))
	return f



def calc_sum(y,o,j, i):
	s = 0
	for l in range(len(y)):
		term1 = (y[l] - o[l]) * lambda_o * y[l] * (1-y[l]) * w_jlLIST[j][l]
		term2 = lambda_h * z_jLIST[j] * (1 - z_jLIST[j]) * xLIST[i]
		s += term1 * term2
	return s



net_j = np.matmul(np.matrix.transpose(w_ij), np.matrix.transpose(x))

print(net_j)

z_j = [f_hidden(i[0]) for i in net_j]

print('z_j',z_j)
z_lMAT=np.matrix([i.tolist()[0][0] for i in z_j])

z_jLIST = [i.tolist()[0][0] for i in z_j]
net_l = np.matmul(np.matrix.transpose(w_jl), np.matrix.transpose(z_lMAT))

print(net_l)

out = [f_out(i[0]) for i in net_l]

print(out)

y = [i.tolist()[0][0] for i in out]
print(y)

l_rate = -0.5

o = [0.2,0.3]

delta_wij = [[0 for x in range(3)] for y in range(4)]
for i in range(4):
	for j in range(3):
		delta_wij[i][j] = calc_sum(y, o, j, i)

print('\n\n\n')
print(l_rate*np.matrix(delta_wij))

print(w_ij + l_rate*np.matrix(delta_wij))



l_rate_o = -0.8
delta_wjl = [[0 for x in range(2)] for y in range(3)]
for j in range(3):
	for l in range(2):
		delta_wjl[j][l] = l_rate_o * lambda_o * (y[l] - o[l]) * (y[l]) * (1-(y[l])) * z_jLIST[j]


print(delta_wjl)
