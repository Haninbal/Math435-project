import os
import sys
import numpy as np
import time
import main as m

def main(args):
	n = int(args[0]) if len(args) >= 1 else 2000
	ep = float(args[1]) if len(args) >= 2 else 0.06
	bound = float(args[2]) if len(args) >= 3 else 5
	directory = args[3] if len(args) >= 4 else "points"
	num_radii = int(args[4]) if len(args) >= 5 else 200
	
	for x in range(num_radii):
		radius = 0.5*np.tan(x*np.pi/(2*num_radii))
		m.main([radius, n, ep, bound, directory+"\\"+str(x)+"points_"+str(radius)+".csv"])
		
		#time.sleep(0.1)
	
	
	
	
if __name__ == '__main__':
	main(sys.argv[1:])