import matplotlib.pyplot as plt
import matplotlib.gridspec as grispec

gs = grispec.GridSpec(3,3)#绘制成3*3的格子


ax1 = plt.subplot(gs[0,:]) #第0行的全部
ax2 = plt.subplot(gs[1,:-1])#第1行的第0，1列
ax3 = plt.subplot(gs[1:,-1])
ax4 = plt.subplot(gs[2, 0])
ax5 = plt.subplot(gs[2, 1 ])
plt.show()
