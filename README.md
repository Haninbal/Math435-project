# Math435-project
curves and surfaces and points on curves on surfaces


to run:
python main.py r n ep bound filename

r is the radius
n is the "minimum" number of samples
ep is the minimum distance between two "continous" points
bound is the furthest a point can be from the origin and still be included
filename is the name of the output

if none are provided it defaults to 
python main.py 1 2000 0.06 10 points.csv

an example call would be
python main.py 1.5 2000 0.06 10 points-1_5.csv


the output is a spreadsheet to look like
x, y, z, distance, "k"

x, y, z are the euclidean coordinates 
distance is the distance from the previous points ("n/a" if not applicable)
k is the number from [0, n) that was queried into the circle.