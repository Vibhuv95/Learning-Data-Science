# Create a plot comparing **Kohli**, **Rohit Sharma**, and **Sehwag** across 10 years of hypothetical runs.  
# Use:
# - Labels
# - Legends
# - Colors
# - Line styles
# - One custom style

import matplotlib.pyplot as plt
import numpy as np

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
Rohit_Sharma =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

plt.plot(years, kohli, label = 'Kohli', color = 'green', linestyle = '-.')
plt.plot(years, sehwag, label = 'Sehwag', color = 'blue', linestyle = '--')
plt.plot(years, Rohit_Sharma, label = 'Rohit Sharma', color = 'pink', linestyle = ':')
plt.legend()

