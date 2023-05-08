
import matplotlib.pyplot as plt
import numpy as np

times = [ 8.776, 17.8, 9.3, 17.2, 12.1, 86.7, 60.5, 150, 250, 290, 270, 270, 180, 130, 437, 675,
          501, 473, 220, 120, 210, 220, 560, 300, 1148, 1538 ]
reached = [ 20, 20, 20, 20, 20, 17, 20, 19, 19, 18, 19, 19, 19, 17, 13, 16,
            16, 17, 19, 19, 16, 20, 15, 16, 15, 16 ]
obstacles = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ]

# plot
fig, ax = plt.subplots()

# ax.plot( obstacles, times, linewidth=2.0 )
# ax.set_ylabel( "Average runtime on success in ms" )
# ax.set_xlabel( "Number of obstacles" )

ax.bar(obstacles, reached, width=1, edgecolor="white", linewidth=0.7)


plt.show()
