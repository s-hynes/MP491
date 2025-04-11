from quiver import eigen
import numpy as np
import matplotlib.pyplot as plt

def direction_field2(xmin=-5, xmax=5, ymin=-5, ymax=5, num_arrows=9):
    
    x = np.linspace(xmin, xmax, num_arrows)
    y = np.linspace(ymin, ymax, num_arrows)

    if abs(xmax-xmin) >= (ymax-ymin):
        man = x
    elif abs(xmax-xmin) < (ymax-ymin):
        man = y

    xx,yy = np.meshgrid(x,y)

    x_dot = yy*(13-xx**2-yy**2)
    y_dot = 12 - xx*(13-xx**2-y**2)

    A = [   [xx, -yy],
            [1,-xx*yy]]
    
    """
    eigenvectors = eigen(A)[2]
    eigenvalues = eigen(A)[0]"""


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

if __name__=="__main__":
    direction_field2(xmin=-7, xmax=7, ymin=-6, ymax=6, num_arrows=20)