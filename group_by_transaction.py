import pandas as pd
from utils import parse_float


def f(x):
    if "espresso" in x.lower():
        print("Classifying {} as espresso".format(x))
        return "Kaffe"
    elif "ica supermarket" in x.lower():
        print("Classifying {} as ICA".format(x))
        return "ICA"
    else:
        print("Couldn't classify {}".format(x))
        return "Övrigt"


data = pd.read_csv(
    'data.csv',
    usecols=[1, 3],
    converters={'Belopp': parse_float}
)

data = data[data['Belopp'] < 0]  # Only consider withdrawals...

data['Belopp'] = data['Belopp'].map(lambda x: -x)
data['Kategori'] = data['Transaktion'].map(f)

data = data.groupby('Kategori')['Belopp'].sum()

data.sort_values(ascending=False).plot(kind='bar', title='Utgifter')

import matplotlib.pyplot as plt
plt.show()
