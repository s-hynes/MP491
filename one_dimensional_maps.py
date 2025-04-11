import numpy as np                 # These lines import the packages numpy and matplotlib.pyplot
import matplotlib.pyplot as plt
import warnings

def mapping(x_0, r, N:int, map):
    """
    Calculates the value of x_n for N subsequent iterations and returns an array of these values.
    
    Parameters
    ----------
    x_0 :   float
            The initial value of x. 
    r :     float
            The value of the parameter in the map (if there is one).
    N :     int
            The total number of iterations that x will be calculated for.
    map :   function
            The 1d map that will be used. Has to be given in the form of a lambda function, 
            e.g. `lambda r,x: r*x**2`.

    Output
    ------
    X : NDArray[float64]
        An array containing the x_n values after each number of iterations. 
    """

    N = int(N)

    X = np.zeros(N+1)  # Define the array 'X', which will contain the values for the normalised population in different years.
    X[0] = x_0         # Initialise the 0th element of 'X' to be equal to 'x_0', the initial (normalised) population

    for i in range(0,N):
        X[i+1] = map(r, X[i])
    
    return X                        # Returns the array 'X'

def conv(x_0, r, N:int, map):
    """
    Determines if a map converges to a particular value for a given initial x value and parameter. 
    
    Parameters
    ----------
    x_0 :   float
            The initial value of x. 
    r :     float
            The value of the parameter in the map (if there is one).
    N :     int
            The total number of iterations that x will be calculated for.
    map :   function
            The 1d map that will be used. Has to be given in the form of a lambda function, 
            e.g. `lambda r,x: r*x**2`. 
    """
        
    X = mapping(x_0, r, N, map)
    N = int(N)
    
    print("\nFor r = {0:.2f}\n".format(r))  # Print the value of the inputted growth parameter 'r'
    
    j = 0   # Defines the variable 'j', which will be used to count the number of iterations needed for the population
            # to converge to a steady value
    
    warnings.filterwarnings("ignore", ".*scalar divide.*")

    per_diff_func = lambda k,l: abs( (X[k]-X[l]) / (X[l]) )

    tending_to_zero = False
    percent_diff_smaller_than_tol = False

    per_diff_arr = np.zeros(10)

    while not(percent_diff_smaller_than_tol) and not(tending_to_zero) and (j+1 != N):
 
        j += 1     # Increases the index 'j' by one to test the next population value.

        #percent_diff_smaller_than_tol = per_diff_func(j+1, j) <= 1e-5
        #print(per_diff_func(j+1, j), percent_diff_smaller_than_tol)

        try:
            tending_to_zero = (np.abs(X[j+1:j+21]) <= np.full_like(X[j+1:j+21], 1e-12)).all()
        except IndexError:
            tending_to_zero = (np.abs(X[j+1:]) <= np.full_like(X[j+1:], 1e-12)).all()
        
        for i in range(10):
            try:
                per_diff_arr[i] = per_diff_func(j+1+i, j)
            except IndexError:
                per_diff_arr[i] = 1

        

        #A = per_diff_arr <= np.full_like(per_diff_arr, 1e-5)
        #print(per_diff_arr, A, "\n")
        percent_diff_smaller_than_tol = (per_diff_arr <= np.full_like(per_diff_arr, 1e-5)).all()


    w = 10  # Define the variable 'w', used to set the width of the graph below
    h = 4   # Define the variable 'h', used to set the height of the graph below
    
    plt.figure(figsize=( w, h) )   # Create a figure of width 'w' and height 'h' that the graph of population against time
                                   # will be shown on.
    
    t = np.linspace(0, N, N+1)   # Define the array 't', which contains the values for years that will be used to plot the graph of population against time
    
    # If the while loop above iterates through all of the population values and finds that the population does not converge in
    # the number of years modelled, this if statement is true and the the function does not give an answer for convergence.
    if (j+1) == N:
    
        print("Does not converge for the number of iterations modelled")
        plt.plot(t, X, 'b:', marker="o", markersize=3)      # Plots a graph of normalised pop against time
        plt.xlim(-0.05*N, 1.01*N)

    # If the population does converge, this else statement executes. This else statement prints the number of years that the 
    # population takes to converge, and the percentage difference from the population the previous year (as a check).
    else:

        plt.plot(t, X, 'b:', marker="o", markersize=3)      # Plots a graph of x_n against time

        if X[0]==X[1]:
            print("x\u2092={0:.4} is a fixed point so the map \"converges\" after 0 iterations to {0:.4}.".format(X[0]))
            plt.plot(t[0], X[j], 'ro', markersize=6)
        else:
            print("x\u2099 converges after {0} iterations to {1:.4}.".format(j, X[j]))
            plt.plot(t[j], X[j], 'ro', markersize=6)

        if X[j]!=0:
            percent_diff = abs((X[j+1]-X[j])/X[j])
            print("Percentage difference from previous iteration = {0:%}\n".format(percent_diff))
        else:
            print("No percentage difference calculated because the denominator is zero.\n")

        if j!=1: plt.xlim(-0.05*j, j+10)
        else: plt.xlim(-0.05*5*j, 10)
    
    # The code within both the if and else statement plots graph of the population as a function of time, but the else statement
    # for convergent populations also crops this graph more and marks the point at which the population converges with a red dot.
    
    plt.title("Population vs number of iterations for r = {0:.2f} with initial population $x_0$ = {1}".format(r, x_0))
    plt.xlabel("Iterations $n$")                           # Gives the graph its x label
    plt.ylabel("$x_n$")                                    # Gives the graph its y label
    plt.grid()                                             # Adds gridlines to the graph
    plt.show()                                             # Shows the graph

if __name__=="__main__":
    print(mapping.__doc__)
    #conv(0.1, 0.3, 1000, lambda r,x: 4*r*x*(1-x))
    #conv(5, 0.5, 100, lambda r,x: r*x)
    
    #conv(2.2, 0.5, 5000, lambda r,x: x*(x-2))
    #conv(2.2, 0.5, 5000, lambda r,x: x*(x-2))
    pass