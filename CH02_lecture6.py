from quiver import eigen, direction_field
import numpy as np

a = 8

#eigen([ [4, 2], [3, -1]], print_values=True)

#direction_field(3,-4,1,-1, xmin=-10, xmax=10, ymin=-10, ymax=10, num_arrows=45)
#direction_field(1,1,4,-2, xmin=-5, xmax=5, ymin=-10, ymax=10, num_arrows=20)
#direction_field(0,1,-1,0, xmin=-10, xmax=10, ymin=-10, ymax=10, num_arrows=10)
direction_field( 3, a, 1, 1, xmin=-5, xmax=5, ymin=-5, ymax=5, num_arrows=21)