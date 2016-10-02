import pandas as pd
from utils import parse_float
import matplotlib.pyplot as plt


def categorize(x):
    # if "espresso" in x.lower():
    #     return "Kaffe"
    if "ICA SUPERMARKET BROM" in x:
        return "ICA"
    if 'ESPRESSO HOUSE 218' in x:
        return 'Fika'
    if 'Omsättning lån 3065 82 24190' in x:
        return 'Lån'
    if 'BÖNOR O BLAD MOOD' in x:
        return 'Kaffe'
    if 'Autogiro FOLKSAM' in x:
        return 'Räkningar'
    if 'SL BROMMAPLAN T BANA' in x:
        return 'SL'
    if 'Arbetslöshetska' in x:
        return 'Räkningar'
    # elif "ONLINEPIZZA" in x.upper():
    #     return "PIZZA"
    # elif "sbab" in x.lower():
    #     return "SBAB"
    else:
        print('Could not categorize: ' + x);
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
