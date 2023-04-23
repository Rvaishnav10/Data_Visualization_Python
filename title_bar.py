import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8.0,6.0))
names=['A','B','C']
values=[20,50,47]
values2=[10,40,63]
values3=[20,50,45]
ax=fig.add_subplot(131)
ax2=fig.add_subplot(132)
ax3=fig.add_subplot(133)
ax.set_title('Age')
ax2.set_title('year')
ax3.set_title('value')

ax.bar(names, values, color='c')
ax2.bar(names, values2, color='goldenrod')
ax3.bar(names, values3, color='mediumorchid')
plt.suptitle('test plot')

plt.show()
