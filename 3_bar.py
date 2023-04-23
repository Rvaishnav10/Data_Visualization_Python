import matplotlib.pyplot as plt
fig=plt.figure()
names=['A','B','C']
values=[20,50,47]
values2=[10,40,63]
values3=[20,50,45]
ax=fig.add_subplot(131)
ax2=fig.add_subplot(132)
ax3=fig.add_subplot(133)
ax.bar(names, values, color='b')
ax2.bar(names, values2, color='r')
ax3.bar(names, values3, color='g')
plt.show()
