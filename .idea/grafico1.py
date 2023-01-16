import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = pd.read_csv(r'C:\Users\dede\jupyter\questionario.csv',
                  usecols=["1.Qual o seu curso?", "2. Qual o período cursado?"])
repeated = x.groupby(x.columns[0]).size()
plt.pie(repeated)
plt.hist(x.groupby(x.columns[1]).size())

plt.show()
