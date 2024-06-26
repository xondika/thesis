
import matplotlib.pyplot as plt
import numpy as np

times = [ 8.776, 17.8, 9.3, 17.2, 12.1, 86.7, 60.5, 150, 250, 290, 270, 270, 180, 130, 437, 675,
          501, 473, 220, 120, 210, 220, 560, 300, 1148, 1538 ]

times5 = [ 303, 117, 193, 288, 312, 315, 498, 150, 1495, 347, 687, 182, 476, 656, 1713, 1647 ]
reached5 = [ 19, 19, 19, 18, 18, 18, 17, 16, 18, 16, 18, 19, 19, 16, 15, 17 ]
obstacles5 = [ 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,]

# reached = [ 20, 20, 20, 20, 20, 17, 20, 19, 19, 18, 19, 19, 19, 17, 13, 16,
#             16, 17, 19, 19, 16, 20, 15, 16, 15, 16 ]
reached = [100, 100, 100, 100, 100, 89, 98, 95, 95, 90, 96, 95, 95, 85, 69, 80, 80,
           85, 95, 95, 80, 99, 78, 80, 76, 80]

obstacles = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ]

# plot
fig, ax = plt.subplots()

# ax.plot( obstacles5, times5, linewidth=2.0 )
# ax.set_ylabel( "Average runtime on success in ms" )
# ax.set_xlabel( "Number of obstacles" )

ax.bar(obstacles, reached, width=1, edgecolor="white", linewidth=0.7)


plt.show()
