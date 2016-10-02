import pandas as pd
from utils import parse_float
import matplotlib.pyplot as plt

with open('categories.json') as f:
    import json

    categories = json.load(f)


def categorize(tx):
    matches = [category for (category, patterns) in categories.items() if any(pattern in tx for pattern in patterns)]

    if len(matches) > 0:
        raise Exception('Ambiguous pattern, {} matches {}', tx, matches)


    if len(matches) == 1:
        return matches[0]
    else:
        print('Uncategorixed: ' + tx)
        return "Övrigt"


data = pd.read_csv(
    'data.csv',
    usecols=[1, 3],
    converters={'Belopp': parse_float}
)

data = data[data['Belopp'] < 0]  # Only consider withdrawals...
data['Kategori'] = data['Transaktion'].map(categorize)

data = data.groupby('Kategori')['Belopp'].sum()

data.index.name = ''  # TODO: Figure out how to just not plot this instead...
data.sort_values().plot(kind='bar', title='Utgifter'),
plt.gca().invert_yaxis()
plt.show()
