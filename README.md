# Plotting of Nordea tx-dumps

This script will plot a bar chart of transactions categorized according to `categories.json`.

The categories will be considered a match if at least one of the patterns are a substring of the 'Transaktion'-entry of the given transaction

(Actualy, this has more to do with me fooling around with [Pandas](http://pandas.pydata.org) than with Nordea dumps...)

## How?

### Generate `data.csv`

- Download some Nordea dumps
 - rename them: `export.csv` -> `data/export_4_apr.csv` etc.
- Clean up, and merge, the files under `data/`

    ```
    $ {
    echo 'Datum,Transaktion,Kategori,Belopp,Saldo'
    awk 'FNR != 1' data/* \  # Strip csv-header
     | tr -d '\r' \          # Strip DOS newlines
     | sed '/^$/d'           # Strip empty lines
    } > data.csv
    ```

### Run the script
- `$ pyvenv venv`
- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`
- `python group_by_category.py`

#### Sample dump

    $ cat export.example
	Datum,Transaktion,Kategori,Belopp,Saldo
	2016-08-31,Omsättning lån 3065 82 24190,,"-3.402,00","22.131,55"
	2016-08-31,Kortköp 160829 ICA SUPERMARKET BROM,,"-365,09","25.533,55"
	2016-08-31,Kortköp 160829 SKILLCAPPED,,"-42,77","25.898,64"
	2016-08-31,Betalning PG 4176103-2 Fastum,,"-2.835,00","25.941,41"
	2016-08-31,Autogiro BAHNHOF,,"-1.147,00","28.776,41"
	2016-08-31,Autogiro FOLKSAM,,"-318,00","29.923,41"
	2016-08-30,Kortköp 160828 ICA SUPERMARKET BROM,,"-290,64","30.241,41"
	...

#### Example `categories.json`

    $ cat categories.json.example
	{
	  "\"ICA\"": [
	    "ICA SUPERMARKET",
	    "COOP KONSUM BROMMAPL"
	  ],
	  "Kaffe": [
	    "ESPRESSO HOUSE 218",
	    "Espresso House",
	    "BÖNOR O BLAD MOOD",
	    "BARISTASHOPEN SE",
      ...
    }
