import numpy as np

'''
N=6
W=21
table=[]
weight=[0,2,3,4,5,9]
value=[0,3,4,5,8,10]

def initTable(n, w):
	table = np.zeros((N, W), dtype='int')
	return table

if __name__ == '__main__':
	table = initTable(N, W)
#	print(table)

	for i in range(1, N):
		for j in range(1, W):
			if weight[i] > j:
				table[i][j] = table[i-1][j]
			else:
				value1 = table[i-1][j]
				value2 = table[i-1][j-weight[i]] + value[i]
				if value1 > value2:
					table[i][j] = value1
				else:
					table[i][j] = value2

#	print(table[N-1][W-1])

	print(table)
'''

weight=[0,2,3,4,5,9]
value=[0,3,4,5,8,10]

def B(k, w):
	if k <= 0:
		return 0

	if weight[k] > w:
		return B(k - 1, w)

	val1 = B(k - 1, w - weight[k]) + value[k]
	val2 = B(k - 1, w)
	if val1 > val2:
		return val1

	return val2


if __name__ == '__main__':
	print(B(5, 20))




