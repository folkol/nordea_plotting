import pandas as pd
from utils import parse_float
import matplotlib.pyplot as plt

uncategorized = []


def categorize(tx):
    categories = {
        'ICA': ['ICA SUPERMARKET', 'COOP KONSUM BROMMAPL'],
        'Kaffe': ['ESPRESSO HOUSE 218', 'BÖNOR O BLAD MOOD', 'BARISTASHOPEN SE'],
        'iMac': ['Omsättning lån 3065 82 24190'],
        'Hårdvara': ['WEBHALLEN', 'CLAS OHLSON', 'KJELL O CO KUNGSHOLM', 'INET STHLM',
                     'MATERIAL AB', 'WWW IKEA SE', 'KUNGSHOLMENS JERN AB', 'ELGIGANTEN STOC', 'Ventmetoder Väst',
                     'SIBA 45', 'SAHLINS GUMMIVERKSTA'],
        'Boende': ['Fastum', 'Autogiro SBAB', 'BAHNHOF', 'LÄNSFÖRSÄKRINGAR', 'INSTALLERA SW', 'CIRCLE K KARLST'],
        'Räkningar': ['Autogiro FOLKSAM', 'Arbetslöshetska', 'Autogiro ACCEPT FÖRS', 'ENERGIKUNDSERVI'],
        'SL': ['SL BROMMAPLAN T BANA', 'SL SUNDBYBERG PENDEL', 'SL HOTORGET SODRA T', 'SL HAMMARBYHOJDEN',
               '25   HOTORGET S', 'SL GULLMARSPLAN T BA', 'SL GAMLA STAN', 'SL SKANSTULL SODRA'],
        'Motion': ['FITNESS24', 'BEST BIKES SVERIGE'],
        'Pizza': ['pizza', 'pizzeria', 'KLARNA AB'],
        'Köpemat': ['RESTAURANG', 'REST STORA VIKINGENO', 'DAIICHI BROMMA AB', 'MCDONALDS BROMMAPLA',
                    'SANKT ERIKSPLAN TACO', 'FROMAGERIET', 'BUN MEAT BUN SODERHA', 'CAFE EGOISTE',
                    'MAMA YES SUSHI O THA', 'PASCHA DELI', 'SUSHI BAR KIRIN', 'BROD OCH SALT MOOD',
                    'LAO WAI', 'CAFE AVENYN', 'Kortköp 160826 EAT',
                    'PRINCESSKONDITORIET', 'LIMERICK PA DROTTNIN', 'Kortköp 160608 EAT', 'TEXAS LONGHORN',
                    'ELENAS GRILL'],
        'Öl': ['COPPERFIELDS', 'FOLKBAREN', 'PONG', 'PUB ANCHOR', 'SYSTEMBOLAGET STOCKH', 'THE DUBLINER AB',
               'THE LIFFEY', 'ENGELEN KOLINGEN', 'WIRSTRÖMS PUB', 'SYSTEMBOLAGET BROMMA'],
        'Mjukvara': ['ADOBE  PHOTOGPHY PLA', 'Amazon web services', 'BLIZZARD ENTERTAIN', 'ITUNES COM BILL',
                     'UFC TV', 'SKILLCAPPED', 'TUC* RealNames com', 'WWW VIAPLAY SE', 'SPOTIFY',
                     'DIGITAL RIVER IRELAN', 'Vardagspaketet', 'APRESS'],
        'Telefon': ['Hi3G', 'Betalning BG 319-9973 3'],
        'Lån': ['72651624578', 'Träningskort 7265 16 24578'],
        'CSN': ['Centrala Studie'],
        'Taxi': ['TAXI STOCKHOLM'],
        'Apotek': ['Apotek', 'Kortköp 160409 SVEA'],
        'Kort': ['Vardagspaketet Aug'],
        'Tandläkare': ['FOLKTANDVARDEN'],
        'Events': ['TRIPPUS', 'CONFETTI EVENTS'],
        'Småprylar': ['OOB SVEAVAGEN', 'CERVERA REGERINGSGAT', 'AKADEMIBOKHANDELN AB', 'OFFICE DEPOT SVENSKA'],
        'Magasin': ['Bonnier Publicat'],
        'Kläder': ['GARDEROBEN SWED', 'H M 033 STOCKHOLM'],
        'Nöje': ['FJERILSHUSET HAGA TR', 'ULRIKSDALS SLOTT', 'SF BIO  RIGOLETTO'],
        'Pressbyrån': ['7 ELEVEN 4316110', 'Pressbyrån', 'OKQ8', 'SHOP N GO', 'WB COFFEE SHOP', 'SWEET HOUSE'],
        'Resor': ['INGO RIMFORSA'],
        'Swish': ['Swish betalning']
    }

    for category, patterns in categories.items():
        if any(pattern.lower() in tx.lower() for pattern in patterns):
            return category
    else:
        uncategorized.append(tx)
        return "Övrigt"


data = pd.read_csv(
    'data.csv',
    usecols=[1, 3],
    converters={'Belopp': parse_float}
)

data = data[data['Belopp'] < 0]  # Only consider withdrawals...
data['Kategori'] = data['Transaktion'].map(categorize)

if uncategorized:
    print('\n'.join(uncategorized))
    print('{} transactions not categorized.'.format(len(uncategorized)))

data = data.groupby('Kategori')['Belopp'].sum()

data.index.name = ''  # TODO: Figure out how to just not plot this instead...
data.sort_values().plot(kind='bar', title='Utgifter'),
plt.gca().invert_yaxis()
plt.show()
