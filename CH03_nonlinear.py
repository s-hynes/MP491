"""This is a version of the function that plots direction fields that works for nonlinear ODEs.
I think that it could eventually be merged with the function for the linear case."""

from CH02_quiver import eigen
import numpy as np
import matplotlib.pyplot as plt

def direction_field2(xdot, ydot, xmin=-5, xmax=5, ymin=-5, ymax=5, num_arrows=9):
    
    x = np.linspace(xmin, xmax, num_arrows)
    y = np.linspace(ymin, ymax, num_arrows)

    if abs(xmax-xmin) >= (ymax-ymin):
        man = x
    elif abs(xmax-xmin) < (ymax-ymin):
        man = y

    xx,yy = np.meshgrid(x,y)

    x_dot = xdot(xx, yy)
    y_dot = ydot(xx, yy)


    fig1, ax1 = plt.subplots()

    ax1.quiver(xx, yy, x_dot, y_dot)
    #ax.plot(x, np.zeros_like(x), 'gray')
    """
    for i in range(2):
        if np.isreal(eigenvalues[i]):
            if eigenvalues[i] > 0:
                ax.plot( np.real(eigenvectors[i,0])*man, np.real(eigenvectors[i,1])*man, 'r--', label='Unstable manifold')
            elif eigenvalues[i] < 0:
                ax.plot( np.real(eigenvectors[i,0])*man, np.real(eigenvectors[i,1])*man, 'g--', label='Stable manifold')
            ax.legend()
    """
    ax1.grid()
    ax1.set_xlim(xmin, xmax)
    ax1.set_ylim(ymin, ymax)
    plt.show()


def stream(xdot, ydot, xmin=-5, xmax=5, ymin=-5, ymax=5, num_points=100, eq_pts=[]):

    eq_pts = np.array(eq_pts)

    x = np.linspace(xmin, xmax, num_points)
    y = np.linspace(ymin, ymax, num_points)

    xx,yy = np.meshgrid(x,y)

    x_dot = xdot(xx, yy)
    y_dot = ydot(xx, yy)

    #x_eq = np.empty_like(x_dot)
    #y_eq = np.empty_like(y_dot)

    fig = plt.figure(figsize=(10,10))


    plt.streamplot(xx, yy, x_dot, y_dot, density=1)
    try:
        plt.plot(eq_pts[:,0], eq_pts[:,1], 'ko')
    except:
        pass

    plt.axis("equal")
    plt.grid()
    plt.show()

if __name__=="__main__":
    #direction_field2(xdot=lambda x,y: y*(13-x**2-y**2), ydot=lambda x,y: 12 - x*(13-x**2-y**2), xmin=-7, xmax=7, ymin=-6, ymax=6, num_arrows=20)
    #direction_field2(xdot=lambda x,y: x - y, ydot=lambda x,y: 1 - x*y, xmin=-10, xmax=10, ymin=-10, ymax=10, num_arrows=25)
    stream(xdot=lambda x,y: x - y, ydot=lambda x,y: 1 - x*y, xmin=-4, xmax=4, ymin=-4, ymax=4, eq_pts=[ [-1,-1], [1,1]])