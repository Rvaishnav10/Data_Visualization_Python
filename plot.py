import matplotlib.pyplot as plt
import numpy as np
import math

range =np.arange(0, math.pi*2, 0.25)
sin=np.sin(range)
fig=plt.figure()
ax=fig.add_axes([0.1, 0.1, 0.75, 0.75])
ax.plot(range, sin)
ax.set_xlabel('X axis')
ax.set_ylabel('y axis')
ax.set_title('Sine')
ax.set_xticks([0,2,4,6,8])
ax.set_xticklabels(['zero','two', 'four','six','eight'])
ax.set_yticks([-1,0,1])

plt.show()
