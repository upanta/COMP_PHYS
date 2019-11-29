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



def calc_sum(y,o,j, i, z_jLIST):
	s = 0
	for l in range(len(y)):
		term1 = (y[l] - o[l]) * lambda_o * y[l] * (1-y[l]) * w_jlLIST[j][l]
		term2 = lambda_h * z_jLIST[j] * (1 - z_jLIST[j]) * xLIST[i]
		s += term1 * term2
	return s


with open('temperature.dat') as datafile:
	temp = datafile.readlines()


data = [x.strip() for x in temp]
DATA = [float(x) for x in data]
#print(DATA)



def update(x, o, w_ij,w_jl, update_weights):
	net_j = np.matmul(np.matrix.transpose(w_ij), np.matrix.transpose(x))
	
	
	z_j = [f_hidden(i[0]) for i in net_j]
	
	z_lMAT=np.matrix([i.tolist()[0][0] for i in z_j])
	
	z_jLIST = [i.tolist()[0][0] for i in z_j]
	net_l = np.matmul(np.matrix.transpose(w_jl), np.matrix.transpose(z_lMAT))
	
	
	out = [f_out(i[0]) for i in net_l]
	
	
	y = [i.tolist()[0][0] for i in out]
	
	l_rate = -0.5
	
	
	

	if update_weights:
		delta_wij = [[0 for x in range(3)] for y in range(4)]
		for i in range(4):
			for j in range(3):
				delta_wij[i][j] = l_rate * calc_sum(y, o, j, i, z_jLIST)
		
		print('\n\n\n')
		
		print('w_ij\n',w_ij + l_rate*np.matrix(delta_wij))
		
		
		
		l_rate_o = -0.8
		delta_wjl = [[0 for x in range(2)] for y in range(3)]
		for j in range(3):
			for l in range(2):
				delta_wjl[j][l] = l_rate_o * lambda_o * (y[l] - o[l]) * (y[l]) * (1-(y[l])) * z_jLIST[j]
		
		
	
		return delta_wij, delta_wjl
	else:
		return net_l


def main(data, wij, wjl):
	length_of_training_set = 4
	update_weights = True
	for i in range(int(len(DATA)*0.6)):
		x = np.matrix(DATA[i:i+length_of_training_set])
		o = DATA[i+length_of_training_set+1:i+length_of_training_set+3]	
		for j in range(20):
#			x = np.matrix([0.1,0.2,0.3,0.4])
			print(x)	
			delta_wij, delta_wjl = update(x, o, wij, wjl, update_weights)
			
	
			wij = wij + np.matrix(delta_wij)
			print('w_ij\n', wij)	
			wjl = wjl + np.matrix(delta_wjl)
			print('\n\nw_jl\n', wij)	
#		break
#	break
	print('final\n')
	print(wij)
	print('\n\n',wjl)

	print('\n\n\n\n\nDONE UPDATING\n\n\n\n\n')	

	update_weights = False
	for i in range(int(len(DATA)*0.4-length_of_training_set)):
		index = int(len(DATA)*0.6)
		x = np.matrix(DATA[index+i:index+i+length_of_training_set])
		
		predicted = update(x, o, wij, wjl, update_weights)
		actual = DATA[index+i+length_of_training_set+1:index+i+length_of_training_set+3]
		print('Predicted value\n', predicted)
		print('Actual Value\n', actual)

main(data, w_ij, w_jl)
