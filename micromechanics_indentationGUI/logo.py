""" draw the logo of the GUI """
import matplotlib.pylab as plt
import numpy as np

row = column = 3
Hardness=np.ones((row,column))
Hardness0 =10
Hardness_Decrease=0.2
for i in range(row):
  for j in range(i,column):
    Hardness[i,j] = Hardness[j,i] = Hardness0 - (j+i)/2+Hardness_Decrease

linewidth=10
color='white'
plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()
#plot mapping
ax.imshow(Hardness, cmap='Blues', vmin=np.min(Hardness)-0.1*Hardness0, vmax=np.max(Hardness))
#surface finding
x_ = np.arange(-0.5,0,0.01)
y_ = np.ones(len(x_)) * 0 + row -0.5
ax.plot(x_,y_,linewidth=linewidth,color=color)
#lot loading
x_ = np.arange(0,row-0.55+0.01,0.01)
C = (row) / (row-0.55)**2
y_ = -C * x_**2 + row -0.5
ax.plot(x_,y_,linewidth=linewidth,color=color)
#plot holing
x_ = np.arange(row-0.55,row-0.5,0.0001)
y_ = np.ones(len(x_)) * -0.5
ax.plot(x_,y_,linewidth=linewidth,color=color)
#plot unloading
alpha=5
hf = row-0.5-(row/alpha)**(1/1.25)
print(hf)
x_ = np.arange(hf,row-0.5,0.0001)
y_ = -alpha * (x_ -hf) ** 1.25 + row -0.5
ax.plot(x_, y_,linewidth=linewidth,color=color)
#surface finding
x_ = np.arange(0,hf,0.01)
y_ = np.ones(len(x_)) * 0 + row -0.5
ax.plot(x_,y_,linewidth=linewidth,color=color)
#plot grid
for i in range(row-1):
  ax.axvline (i+0.5, color='white', linewidth=5)
  ax.axhline (i+0.5, color='white', linewidth=5)
#remove frame
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
fig.savefig('logo.png',dpi=1000)
