import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[2,3,5,7,8,9,2,5,6]

plt.scatter(x,y,label="stars", color="cyan", marker="*", s=30)

plt.xlabel('x axis')
plt.ylabel('y label')
plt.title("test bar")
plt.legend()
plt.show()
