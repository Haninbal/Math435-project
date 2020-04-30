import numpy as np


class circle:
	def __init__(self, r=1, n=2000):
		self.r = float(r)
		self.n = int(n)
		
	def eval(self, k):
		t = k*2*np.pi/self.n
		return [self.r*np.cos(t), self.r*np.sin(t)]
		
	def __str__(self):
		return "circle with radius "+str(self.r)+" and "+str(self.n)+ " samples"