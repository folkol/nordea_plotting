import pandas as pd
from matplotlib import pyplot as plt
from utils import parse_float

pd.read_csv(
    'data.csv',
    usecols=['Datum', 'Belopp'],
    converters={'Belopp': parse_float}
).groupby('Datum').sum().cumsum().plot()

plt.show()
