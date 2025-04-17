from CH03_nonlinear import stream
import numpy as np
import matplotlib.pyplot as plt

def stream_pol(rdot, thetadot, xmin=-5, xmax=5, ymin=-5, ymax=5, num_points=100, eq_pts=[], density=1):

    eq_pts = np.array(eq_pts)

    x = np.linspace(xmin, xmax, num_points)
    y = np.linspace(ymin, ymax, num_points)

    xx,yy = np.meshgrid(x,y)

    r = np.sqrt(xx**2 + yy**2)
    theta = np.atan(yy/xx)

    x_dot = -yy*thetadot(r,theta) + xx/(np.sqrt(xx**2 + yy**2))*rdot(r,theta)
    y_dot = xx*thetadot(r,theta) + yy/(np.sqrt(xx**2 + yy**2))*rdot(r,theta)

    fig = plt.figure(figsize=(6.5,6.5))

    plt.streamplot(xx, yy, x_dot, y_dot, density=density)
    try:
        plt.plot(eq_pts[:,0], eq_pts[:,1], c='grey', linestyle='', marker='o', markersize=5)
    except:
        pass

    plt.axis("equal")
    plt.grid(alpha=1/2)
    plt.show()

if __name__=="__main__":
    stream_pol(lambda r,theta: r*(1-r**2), lambda r,theta: 1, xmin=-2, xmax=2, ymin=-2, ymax=2, eq_pts=[[0,0]])