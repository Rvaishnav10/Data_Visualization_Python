import matplotlib.pyplot as plt
fig=plt.figure(figsize=(15.0,6.0))
names=['A','B','C']
values=[20,50,47]
values2=[10,40,63]

ax=fig.add_subplot(131)
ax2=fig.add_subplot(132)

ax.set_title('Age')
ax2.set_title('year')
ax.set_xlabel('year')
ax.set_ylabel('value')
ax2.set_xlabel('year')
ax2.set_ylabel('value')
ax.bar(names, values, color='c')
ax2.bar(names, values2, color='m')

plt.suptitle('test plot')
plt.show()
