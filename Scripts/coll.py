import matplotlib.pyplot as plt
labels = 'Matrix computation', 'Collision checking'
sizes = [2230311 - 1630099, 1630099]

plt.rcParams.update({'font.size': 15})
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['#1f77b4', '#2ca02c'], startangle = 180, counterclock = False,
       labeldistance=1.1)

plt.show()
