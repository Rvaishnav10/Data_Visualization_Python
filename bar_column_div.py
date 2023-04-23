import matplotlib.pyplot as plt
fig=plt.figure()
names=['A','B','C']
values=[20,50,47]
values2=[10,40,63]
ax=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax.bar(names, values, color='b')
ax2.bar(names, values2, color='r')
plt.show()
