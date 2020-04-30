import sys
import circle as cir
import numpy as np

def to_output(point):
	#pass
	print(str(point))
	
def floor(k):
	if int(k) == k:
		return k-1
	else:
		return int(k)
	
def euclidean_distance(x, y, z):
	return np.sqrt(x**2 + y**2 + z**2)

def function(y):
	x0 = -4 * (4*(y[0]**2)  -   (y[1]**2) - (y[2]**2)) * y[0]
	x1 = -1 * (16*(y[0]**2) - 4*(y[1]**2) + (y[2]**2)) * y[1]
	x2 = 1  * (4*(y[0]**2)  + 4*(y[1]**2) - (y[2]**2)) * y[2]
	x3 = 10*y[0]*y[1]*y[2]
	
	return [x0, x1, x2, x3]
	
def mapping(cirpoint, c, r, n, ep, bound, last, k):
	y = cirpoint + [int(r)]
		
	X = function(y)
	if abs(X[3] > 1e-10):
		x, y, z = X[0]/X[3], X[1]/X[3], X[2]/X[3]
		if euclidean_distance(x, y, z) < bound:
			if last is not None: 
				d = euclidean_distance(x-last[0], y-last[1], z-last[2])
				if d > ep:
					nk = (k+floor(k)) / 2
					'''if abs(nk -k) < 1e-6:
						break '''
					#print(str(k)+" "+str(floor(k))+" "+str(nk))
					k = nk
					cirpoint = c.eval(nk)
					last = mapping(cirpoint, c, r, n, ep, bound, last, nk)
					if last is not None:
						to_output(last)
						d = euclidean_distance(x-last[0], y-last[1], z-last[2])
					'''else:
						break '''
			else:
				d = "n/a"
			return [x, y, z, d]
	return None

def main(args):
	print("hello world")
	r = float(args[0]) if len(args) >= 1 else 1
	n = int(args[1]) if len(args) >= 2 else 2000
	ep = float(args[2]) if len(args) >= 3 else 0.06
	bound = float(args[3]) if len(args) >= 4 else 10
	c = cir.circle(args[0], args[1])
	last = None
	
	
	for k in range(n):
		cirpoint = c.eval(k)
		last = mapping(cirpoint, c, r, n, ep, bound, last, k)
		if last is not None:
			to_output(last)
	

if __name__ == '__main__':
	main(sys.argv[1:])