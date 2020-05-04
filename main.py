import sys
import circle as cir
import numpy as np

_last = None
_filename = None

def setup_output(filename):
	global _filename
	
	with open(filename, "w+") as f:
		f.write("")
		_filename = filename
		

def to_output(point):
	global _filename
	
	with open(_filename, "a") as f:
		f.write(str(point)[1:-1]+ "\n")
	
	
def set_last(k):
	global _last 
	_last = k
	#print(k)
	
def floor(k):
	global _last
	return _last
	
def euclidean_distance(x, y, z):
	return np.sqrt(x**2 + y**2 + z**2)

def function(y):
	x0 = -4 * (4*(y[0]**2)  -   (y[1]**2) - (y[2]**2)) * y[0]
	x1 = -1 * (16*(y[0]**2) - 4*(y[1]**2) + (y[2]**2)) * y[1]
	x2 = 1  * (4*(y[0]**2)  + 4*(y[1]**2) - (y[2]**2)) * y[2]
	x3 = 10*y[0]*y[1]*y[2]
	
	return [x0, x1, x2, x3]
	
def compute_point(cirpoint, r):
	y = cirpoint + [1]
	#print(y)
	X = function(y)
	#print(X)
	if abs(X[3] > 1e-20):
		x, y, z = X[0]/X[3], X[1]/X[3], X[2]/X[3]
		#print(str(x)+" "+str(y)+" "+str(z))
		return [x, y, z]
	return None
	
def interpolate_points(c, r, n, ep, bound, left_point, right_point, beg_k, mid_k, end_k):	
	if beg_k == mid_k or beg_k >= end_k:
		#print("max depth reached in interpolate_points, something went wrong: beg_k="+str(beg_k))
		return None
	cirpoint = c.eval(mid_k)
	p = compute_point(cirpoint, r)
	if p is None:
		return None
	
	x, y, z = p[0], p[1], p[2]
	if euclidean_distance(x, y, z) < bound:
		d = euclidean_distance(x-left_point[0], y-left_point[1], z-left_point[2])
		if d > ep: #add any points that need to be added prior to the point
			try:
				lm_point = interpolate_points(c, r, n, ep, bound, left_point, p, beg_k, (beg_k+mid_k)/2, mid_k)
			except RecursionError as e:
				lm_point = None
				
			if lm_point is not None:
				d = euclidean_distance(x-lm_point[0], y-lm_point[1], z-lm_point[2])
			
		to_output(p + [d, mid_k*2*np.pi/n]) #add the point 
		
		d = euclidean_distance(x-right_point[0], y-right_point[1], z-right_point[2])
		rm_point = None
		if d > ep: #addany points that need to be added after the point 
			try:
				rm_point = interpolate_points(c, r, n, ep, bound, p, right_point, mid_k, (mid_k+end_k)/2, end_k)
			except RecursionError as e:
				rm_point = None
			
		return rm_point if rm_point is not None else p
	else:
		return
			
				
	
def mapping(cirpoint, c, r, n, ep, bound, last, k):
	p = compute_point(cirpoint, r)
	if p == None:
		return
	x, y, z = p[0], p[1], p[2]
	
	if euclidean_distance(x, y, z) < bound:
		if last is not None: 
			d = euclidean_distance(x-last[0], y-last[1], z-last[2])
			if d > ep:
				r_point = interpolate_points(c, r, n, ep, bound, last, p, k-1, k-0.5, k)
				if r_point is not None:
					d = euclidean_distance(x-r_point[0], y-r_point[1], z-r_point[2])
		else:
			d = 0
		set_last(k)
		return p + [d]
	return None

def main(args):
	#print("hello world")
	r = float(args[0]) if len(args) >= 1 else 1
	n = int(args[1]) if len(args) >= 2 else 2000
	ep = float(args[2]) if len(args) >= 3 else 0.06
	bound = float(args[3]) if len(args) >= 4 else 10
	filename = args[4] if len(args) >= 5 else "points.csv"
	
	if "test" in args:
		c = cir.circle(r, n)
		print(c)
		p = compute_point(c.eval(40), r)
		print(p)
		c = cir.circle(0.9, n)
		print(c)
		p = compute_point(c.eval(40), 0.9)
		print(p)
		return
	
	print("radius: "+str(r)+" number of points: "+str(n)+" epsilon: "+str(ep)+" bound: "+str(bound))
	
	setup_output(filename)
	
	c = cir.circle(r, n)
	last = None
	
	
	for k in range(n):
		cirpoint = c.eval(k)
		temp = mapping(cirpoint, c, r, n, ep, bound, last, k)
		if temp is not None:
			to_output(temp+[k*2*np.pi/n])
			last = temp
		else:
			pass
			#print("input of "+str(k)+" was not in the valid area")
	

if __name__ == '__main__':
	main(sys.argv[1:])