def parse_float(number_string):
    """Parses a Nordea–exported number string as a float.

    Unfortunately, `babel.numbers.parse_number` and the Nordea
    export service do not agree upon thousands separators...
    """
    return float(number_string.replace('.', '').replace(',', '.'))
