import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statistics
from statsmodels import robust


df_with_NaN = pd.read_csv("data-2.csv")

df = df_with_NaN.dropna()

df.describe()

vpi = df.Verbraucherpreisindex
years = df.Jahre

vpi_mean = round(np.mean(vpi),3)
vpi_mode = stats.mode(vpi)
vpi_median = statistics.median(vpi)

vpi_spannweite = round(vpi.max() - vpi.min(),3)

vpi_stichprobenvarianz = round(np.nanvar(vpi), 3)

vpi_mam = round(robust.mad(vpi),3)

vk = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
vpi_variationskoeffizient = round(vk(vpi),3)

qt1 = np.percentile(vpi, 25)
qt2 = np.percentile(vpi, 50)
qt3 = np.percentile(vpi, 75)

dz1 = np.percentile(vpi, 10)
dz2 = np.percentile(vpi, 20)
dz3 = np.percentile(vpi, 30)
dz4 = np.percentile(vpi, 40)
dz5 = np.percentile(vpi, 50)
dz6 = np.percentile(vpi, 60)
dz7 = np.percentile(vpi, 70)
dz8 = np.percentile(vpi, 80)
dz9 = np.percentile(vpi, 90)
dz10 = np.percentile(vpi, 100)

dz_sum = [dz1, dz2, dz3, dz4, dz5, dz6, dz7, dz8, dz9]

qt_Abstand = round(qt3 - qt1, 3)

cv = np.cov(years, vpi) [0][1]

plt.boxplot(vpi)
plt.title("Box Whisker Plot")
plt.ylabel("Verbraucherpreisindex")
plt.show()

plt.scatter(vpi, years)
plt.title("Scatterplot")
plt.xlabel("VPI")#
plt.ylabel("Jahre")
plt.show()

plt.bar(years, vpi)
plt.title("Barplot")
plt.ylabel("VPI")#
plt.xlabel("Jahre")
plt.show()

#%%
