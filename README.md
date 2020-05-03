# Math435-project
curves and surfaces and points on curves on surfaces


to run for a single curve:
python main.py r n ep bound filename

r is the radius
n is the "minimum" number of samples
ep is the minimum distance between two "continuous" points
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


to run for multiple curves:
first, create a directory for convience sake (something like "points")
python master.py n ep bound directory num_radii

n is the "minimum" number of points on each curve
ep is the minimum distance between two "continuous" points
bound is the furthest a point can be from the origin and still be included
directory is the directory created to store curve information
num_radii is the number of radii that should be turned into curves, note than at least some of the curves will contain 0 points if bound is a reasonable size

if no arguments are provided it defaults to
python master.py 2000 0.06 5 points 200
which may fail if there is no points directory

an example call would be
mkdir storage
python master.py 2000 0.06 10 storage 100

Note: there is a known glitch for radii about 0.5 where points are put in the output more than once.
No idea what that is about

curves will be saved in directory with the filename npoints_radius.csv where n is simply an integer to make sure that on windows the appear in numerical order.

