# Plots of VMC vs Hybrid architecture

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#Exact_Es = {'4':-0.4534132086591546,'8':-0.40518005298872917,'12':-0.3884864748124427,'16':-0.380514770608724}

noisedata = np.load('Energy-noise-1100.npy')
perfectdata = np.load('Energy-perfect-1100.npy')
vmcdata = np.load('Energy-VMC-1100.npy')
noisevar = np.load('Variance-noise-1100.npy')
perfectvar = np.load('Variance-perfect-1100.npy')
vmcvar = np.load('Variance-VMC-1100.npy')

exact_energy = -0.4534132086591546

colorlist = ['darkblue', 'steelblue', 'lightsteelblue']

fig, axis = plt.subplots(1,1)
figure(figsize=(10,6),dpi=80)

#axis = ax[0]
start = 50
xvals = np.arange(start,len(noisedata)-1,1)
axis.plot(xvals,noisedata[start:-1],marker='o',markersize=1.5,linewidth=0.0,markevery=1,label="Hybrid Model with Noisy Data",color=colorlist[0])
axis.plot(xvals,perfectdata[start:-1],marker='o',markersize=1.5,linewidth=0.0,markevery=1,label="Hybrid Model with Perfect Data",color=colorlist[2])
axis.plot(xvals,vmcdata[start:-1],marker='o',markersize=1.5,linewidth=0.0,markevery=1,label="VMC",color=colorlist[1])
#axis.hlines(exact_energy,0, total_epochs,linestyle="--",label="True Energy",color = 'red')
axis.axvline(x=300,linestyle="--",label="Change Loss Function",color = 'red')
axis.axhline(y=exact_energy, linestyle="--",label="True Energy",color = 'red')
axis.set_xlabel("Step")
axis.set_ylabel("$\\langle H \\rangle$")
axis.set_title("4x4 Energy")
axis.legend(loc = "best")

# axis = ax[1]
# axis.plot(noisevar[50:-1],marker='o',markersize=1.5,linewidth=0.0,markevery=1,label="Hybrid Model with Noisy Data",color=colorlist[2])
# axis.plot(noisevar[50:-1],marker='o',markersize=1.5,linewidth=0.0,markevery=1,label="Hybrid Model with Perfect Data",color=colorlist[0])
# axis.plot(noisevar[50:-1],marker='o',markersize=1.5,linewidth=0.0,markevery=1,label="VMC",color=colorlist[1])
# axis.set_xlabel("Step")
# axis.set_ylabel("$\\langle H \\rangle$")
# axis.set_title("4x4 Variance")
# axis.legend(loc = "best")

fig.savefig('4x4comparision-1100.pdf')




print(noisedata)
