# %%
"""This still needs to be able to incorporate taking different fuctions as an argument. It also
can't deal with half stable points or functions with no fixed points. I also need to adjust the number of
fixed points that it expects to find manually, which isn't ideal."""

import numpy as np                 
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import fsolve, fixed_point, root
import sympy

def stability(f, x0, r_arg, print_stability=False):
    """Determines the stability of a fixed point. Returns +1 for a stable fixed point, -1 for an unstable fixed
    point, and 0 if neither.

    f : A function of x with parameter r

    x0 : Fixed point or points to test
    
    r_arg : inputted parameter r
    
    print_stability : If set to "True", prints the stability of the fixed point. Set to "False" by default."""

    x, r = sympy.symbols('x r')

    f = sympy.sympify(f)

    #f = x - r*(1-x)*x
    #f = 5 - r*sympy.exp(- (x**2) )
    f.subs([(x, x0), (r, r_arg)])
    f_der = sympy.diff(f, x)
    if abs(f.subs([(x, x0), (r, r_arg)])) <= 5e-6:

        #print("f''(x) = {}".format(f_der.subs([(x, x0), (r, r_arg)])))

        if f_der.subs([(x, x0), (r, r_arg)]) < 0:
            if print_stability == True:
                print("{0} is a stable fixed point.".format(x0))
            return +1
        elif f_der.subs([(x, x0), (r, r_arg)]) > 0:
            if print_stability == True:
                print("{0} is an unstable fixed point.".format(x0))
            return -1
    else:
        #print("Stability function doesn't think this is a root.")
        return 0
        # This still needs something to accommodate half stable points.

#stability("x**2 - r", +2, 4, print_stability=True)
# Stability is able to take functions in string format. Bifurc is only able to take them as lambda functions.

#assert 0, "Sin togha boss man."

def bifurc(f, fstring, rmin=-5, rmax=5, rstep=0.01):

    r_arr = np.arange(rmin, (rmax+rstep), rstep)

    x0_guesses = np.array([-100, -5, -0.5, +0.5, +5, +100, 0.01])

    eq_points = np.zeros([2, x0_guesses.shape[0], r_arr.shape[-1]])

    x, r = sympy.symbols('x r')

    not_root = int(0)

    # The i for loop iterates through values of the parameter r.
    for i in range(r_arr.shape[-1]):
        f2 = f(r_arr[i])
        #f = lambda x: x - r_arr[i]*(1-x)*x
        #f = lambda x: 5 - r_arr[i]*np.exp( -(x**2) )
        eq_points[1,:,i] = root(f2, x0_guesses).x

        # The j for loop iterates through the equilibrium points of the function.
        for j in range(eq_points.shape[1]):
            #print(stability(eq_points[1,j,i], r_arr[i]))
            eq_points[0,j,i] = stability(fstring, eq_points[1,j,i], r_arr[i])


        if 0 in eq_points[0,:,i]:
            not_root += 1
            #print(eq_points[1,:,i])
            #print(eq_points[0,:,i])
        
    print("Number of points that stability function thinks aren't roots = {0}".format(not_root))

        # Basically, I want to have a condition here that tests whether or not the fixed point is stable or
        # unstable. I'm thinking that it would rely on differentiating f, then evaluating it at the equilibrium point.
        # If f'(x)>0, the equilibrium point is unstable, and if f'(x)<0 it's unstable.

    return eq_points, r_arr


def plotter(f, fstring, rmin=-5, rmax=5, rstep=0.01, plot_non_eq=False):
    
    data = bifurc(f, fstring, rmin, rmax, rstep)

    eq_points_stable = np.zeros(1)
    r_stable = np.zeros(1)
    eq_points_unstable = np.zeros(1)
    r_unstable = np.zeros(1)
    eq_points_something_else = np.zeros(1)
    r_something_else = np.zeros(1)

    for i in range(data[1].shape[-1]):
        for j in range(data[0].shape[1]):
            #print(data[0][0,j,i])
            if data[0][0,j,i]==+1:
                eq_points_stable = np.append(eq_points_stable, data[0][1,j,i])
                r_stable = np.append(r_stable, data[1][i])
            elif data[0][0,j,i]==-1:
                eq_points_unstable = np.append(eq_points_unstable, data[0][1,j,i])
                r_unstable = np.append(r_unstable, data[1][i])
            else:
                eq_points_something_else = np.append(eq_points_something_else, data[0][1,j,i])
                r_something_else = np.append(r_something_else, data[1][i])

    plt.grid()
    plt.plot(r_stable[1:], eq_points_stable[1:], 'g.')
    plt.plot(r_unstable[1:], eq_points_unstable[1:], 'r.')
    if plot_non_eq==True:
        plt.plot(r_something_else[1:], eq_points_something_else[1:], 'b.')
    plt.xlabel("r")
    plt.ylabel("x* (Fixed Point)")
    plt.show()

#plotter( (lambda r: (lambda x: x**2 - r)), fstring="x**2-r",rmin=-10, rmax=10, rstep=0.01)

"""
for i in range(data[0].shape[1]):
    for j in range(data[0].shape[2]):
        if abs(data[0][1, i, j]) < 99:
            print(data[0][1, i, j])
"""

if __name__=="__main__":
    plotter(lambda r: (lambda x: x**2 + r), "x**2 + r")
