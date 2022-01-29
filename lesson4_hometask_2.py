from requests import get, utils

response = get('https://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(valutes):
    valute = content.split('/Valute')

    for i in valute:
        if valutes in i:
            price = i.split('<Value>')[1].split('</Value>')[:1]
            pricea = ''.join(price)
            print(f"{valutes} {float(pricea.replace(',', '.')):.2f}")

currency_rates('USD')