- Download some Nordea dumps
 - rename them `export.csv` -> `data/export_4_apr.csv` etc.
- Clean up, and merge, the files under `/data`

    ```
    $ {
    echo 'Datum,Transaktion,Kategori,Belopp,Saldo'
    awk 'FNR != 1' data/* \
     | tr -d '\r' \
     | sed '/^$/d'
    } > data.csv
    ```

- `$ pyvenv venv`
- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`
