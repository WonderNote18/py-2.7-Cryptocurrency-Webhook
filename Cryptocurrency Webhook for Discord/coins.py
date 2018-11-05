import requests

"""
Coins Notes
----------------
1 - Bitcoin
52 - Etherium
1027 - Ripple
1993 - Kin
"""

coinDict = {
        '1': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            },
        '52': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            },
        '1027': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            },
        '1993': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            }
        }

def gatherCrypto():
    """
Gathers cryptocurrency informatiom from CMC API into coinDict values.

The function loops through all entries in coinDict and retrieves values based on the name of the .json value from the API.
For price, if the COIN/USD pairing is less than 0.0001, it enables the float value to use up to 8 digits after the decimal, otherwise it uses 4 digits after.
Before going to the next nested dictionary, all integer values are sent through numFormat() to add text formatting to integers
    """
    for key, value in coinDict.items():
        apiURL = 'https://api.coinmarketcap.com/v2/ticker/{}.json'.format(key)
        jsonData = requests.get(apiURL).json()
        value['name'] = jsonData['data']['name']
        value['rank'] = jsonData['data']['rank']
        value['circulation'] = "{:,d}".format(jsonData['data']['circulating_supply'])

        if jsonData['data']['quotes']['USD']['price'] < 0.0001:
            price = '{:,.8f}'.format(jsonData['data']['quotes']['USD']['price'])
            value['USD'] = str(price)
        else:
            price = '{:,.4f}'.format(jsonData['data']['quotes']['USD']['price'])
            value['USD'] = str(price)

        value['volume_24h'] = "{:,f}".format(round(jsonData['data']['quotes']['USD']['volume_24h'], 2))
        value['change_1h'] = jsonData['data']['quotes']['USD']['percent_change_1h']
        value['change_24h'] = jsonData['data']['quotes']['USD']['percent_change_24h']

def resetDict():
    """
    Function used to reset coinDict to original status
    """
    global coinDict
    coinDict = {
        '1': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            },
        '52': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            },
        '1027': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            },
        '1993': {
            'name': '',
            'rank': 0,
            'USD': 0.0,
            'circulation': 0,
            'volume_24h': 0.0,
            'change_1h': 0.0,
            'change_24h': 0.0,
            'url': 'https://coinmarketcap.com/currencies/bitcoin/'
            }
        }

