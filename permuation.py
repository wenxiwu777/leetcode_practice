import numpy as np

def N(n):
	tags = np.ones(n, dtype='int')

	for i in range(1, n**n+1):
		for k in range(n, 1, -1):
			if tags[k-1] > n:
				tags[k-1] = 1
				tags[k-2] = tags[k-2] + 1

		for m in range(0, n):
			print(tags[m], end=' ')
		tags[n - 1] = tags[n - 1] + 1

		print('')

if __name__ == '__main__':
	N(4)