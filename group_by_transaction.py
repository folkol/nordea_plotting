import pandas as pd
from utils import parse_float


def f(x):
    if 'espresso' in x.lower():
        return 'Kaffe'
    elif 'ica' in x.lower():
        return 'ICA'
    else:
        return 'Övrigt'

data = pd.read_csv(
    'data.csv',
    converters={'Belopp': parse_float}
)

data['Kategori'] = data['Transaktion'].map(f)

print(data)

data = data.groupby("Kategori")['Belopp'].first()


print(data)

data.plot(kind='bar')



import matplotlib.pyplot as plt
plt.show()
