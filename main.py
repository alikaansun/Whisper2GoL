import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

from GOL import GameOfLife as gol

den = gol("I love you")
den.initialcond()
print(den.densitycheck())
print(den.iterno)
den.iter()


plt.figure(dpi=150)
heatmap = sns.heatmap(den.cells, linewidths=0.1,square=True)
heatmap.tick_params(left=False, bottom=False)
heatmap.set_yticklabels([])
heatmap.set_xticklabels([])
plt.title(den.seed.capitalize())
plt.show()

