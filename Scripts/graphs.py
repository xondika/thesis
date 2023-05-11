import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

species = ('1st path', '3rd path', '13th path')

times = {
    'Initialization' : [ 23946, 24185, 144733 ],
    'Djikstra' : [ 97, 446, 9613 ],
    'FABRIK' : [ 11435, 881914, 2343671 ],
    'Interpolation' : [ 1298, 16667, 184054 ]
}

totals = [0, 0, 0]
for name, time in times.items():
    for i in range( 3 ):
        totals[ i ] += time[ i ]

for name, time in times.items():
    for i in range( 3 ):
        time[ i ] /= totals[ i ]

width = 0.3  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(3)

for name, time in times.items():
    p = ax.bar(species, time, width, label=name, bottom=bottom)
    bottom += time

    #ax.bar_label(p, label_type='center')

#ax.set_title('Time distribution of a single run')
#ax.set_xlim( 0, 3 )
ax.legend()

#fig.set_figwidth( 3 )
plt.show()
