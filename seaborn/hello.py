import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crash = sb.load_dataset('car_crashes')
crash
crash[0:10]

# Your plotting code
sb.histplot(crash['not_distracted'])

# Display the plot interactively
plt.show()
