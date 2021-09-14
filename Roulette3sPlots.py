import roulette3s as three

import numpy as np
from matplotlib import pyplot as plt 
from decimal import Decimal as D
import random

percent = []
proffit = []
bets = []
x = []
for inc in np.arange(1.05,2.0,.005):
    per,prof,totbet = three.threes(inc,10000,5)
    x.append(inc)
    percent.append(per)
    proffit.append(prof)
    bets.append(totbet)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('bet incriment (factor)')
ax1.set_ylabel('percent win', color=color)
ax1.plot(x, percent, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('amount bet per trial (blue) and net Profit (green) ($)', color=color)  # we already handled the x-label with ax1
ax2.plot(x, bets, color=color)
ax2.tick_params(axis='y', labelcolor=color)

color = 'tab:green'
#ax2.set_ylabel('net profit ($)', color=color)  # we already handled the x-label with ax1
ax2.plot(x, proffit, color=color)


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()