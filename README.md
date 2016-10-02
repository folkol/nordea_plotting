# Plotting of Nordea tx-dumps

This script will plot a bar chart of transactions categorized according to `categories.json`.

(The categories will be considered a match if at least one of the patterns are a substring of the 'Transaktion'-entry of the given transaction...)

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
