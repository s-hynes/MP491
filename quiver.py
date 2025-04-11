
import matplotlib.pyplot as plt
import numpy as np

def eigen(A, print_values=False):
    """This function calculates the eigenvalues and eigenvectors of a square matrix and outputs them in an array. 
    If print_values is set to True it prints them as well as outputting this array.
    
    The 0th element of the output array is a vector containing the eigenvalues, the 1st element is an 
    array containing the eigenvectors, and the 2nd element is an array containing the eigenvectors written more nicely
    by making the smallest element in the array equal to 1."""

    eigval, v = np.linalg.eig(A)
    M = eigval.size
    nice_v = np.zeros_like(v)

    for i in range(M):
        nice_v[i] = (v[:,i])/(np.min(v[:,i]))

    if print_values==True:
        for i in range(M):
            print("\nEigenvalue {0} = {1}, eigenvector {0} = {2}, eigenvector {0} in nicer format = {3}"
                .format(i+1, eigval[i], v[:,i], nice_v[i]))
        print("")
        
    return eigval, v, nice_v

def direction_field(a,b,c,d, xmin=-5, xmax=5, ymin=-5, ymax=5, num_arrows=9):
    
    x = np.linspace(xmin, xmax, num_arrows)
    y = np.linspace(ymin, ymax, num_arrows)

    if abs(xmax-xmin) >= (ymax-ymin):
        man = x
    elif abs(xmax-xmin) < (ymax-ymin):
        man = y

    xx,yy = np.meshgrid(x,y)

    x_dot = a*xx + b*yy
    y_dot = c*xx + d*yy

    A = [   [a,b],
            [c,d]]
    
    eigenvectors = eigen(A)[2]
    eigenvalues = eigen(A)[0]


    fig, ax = plt.subplots()

    ax.quiver(xx, yy, x_dot, y_dot)
    #ax.plot(x, np.zeros_like(x), 'gray')
    #ax.plot(np.zeros_like(y), y, 'gray')
    for i in range(2):
        if np.isreal(eigenvalues[i]):
            if eigenvalues[i] > 0:
                ax.plot( np.real(eigenvectors[i,0])*man, np.real(eigenvectors[i,1])*man, 'r--', label='Unstable manifold')
            elif eigenvalues[i] < 0:
                ax.plot( np.real(eigenvectors[i,0])*man, np.real(eigenvectors[i,1])*man, 'g--', label='Stable manifold')

    #else:
    #    ax.plot( np.real(eigenvectors[i,0])*man, np.real(eigenvectors[i,1])*man)
    for k in range(x.size):

        for l in range(y.size):
            #print(k, l)
            if x_dot[k,l] == 0 and y_dot[k,l] == 0:
                #print("Fixed point at ({0}, {1})".format(x[l], y[k]))
                ax.plot(x[l], y[k], 'ko')    

    ax.legend()
    ax.grid()
    #plt.axis('equal')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    plt.show()

if __name__=="__main__":
    direction_field( 1, 1, 4, -2, xmin=-20, xmax=20, ymin=-20, ymax=20, num_arrows=20)
