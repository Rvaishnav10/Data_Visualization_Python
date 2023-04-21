activities=['eat', 'sleep', 'code', 'repeat']
slices=[3,6,8,10]
colors=['silver','gold','c','olive']

plt.pie(slices, labels= activities, colors=colors, startangle=90, shadow= True, explode=(0,0,0.1,0), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.show()
