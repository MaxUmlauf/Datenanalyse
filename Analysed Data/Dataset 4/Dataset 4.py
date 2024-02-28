import pandas as pd
import numpy as np
from scipy import stats
import statistics
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(0, 10000, size =(130, 1)))

data4 = pd.read_csv("data-4.csv")

values = data4.Value
rows = data4.Row

value_mean = round(np.mean(values),3)
value_mode = stats.mode(values)
value_median = statistics.median(values)

value_stichprobenvarianz = round(np.nanvar(values), 3)

plt.boxplot(values)
plt.title("Box Whisker Plot")
plt.ylabel("Values")
plt.show()
#%%
