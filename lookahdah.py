from bifurcation import plotter

plotter( (lambda r: (lambda x: -1/2 + r*x - x**3)), fstring="-1/2 + r*x -x**3",rmin=-5, rmax=5, rstep=0.01)