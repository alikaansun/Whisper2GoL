import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

from GOL import GameOfLife as gol

den = gol(input("Enter seed: "))
den.initialcond()

print('Number of iterations:',den.iterno)
den.iter()
print('Density',den.densitycheck()/den.size**2)
plt.figure(dpi=150)
heatmap = sns.heatmap(den.cells, linewidths=0.1,square=True,cbar=False)
heatmap.tick_params(left=False, bottom=False)
heatmap.set_yticklabels([])
heatmap.set_xticklabels([])
plt.title(den.seed.capitalize())
plt.show()

