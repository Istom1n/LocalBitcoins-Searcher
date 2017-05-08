#!/usr/bin/python

# Written by Ivan Istomin because

import sys
import requests


def search(options):
    payment_methods = requests.get('https://localbitcoins.net/api/payment_methods/').json()
    type_of_order = options[1]
    currency = options[2]
    name_of_banks = options[3:]

    print 'Type of order: %s\nCurrency: %s\nBanks List: %s' % (type_of_order, currency, str(name_of_banks))

    for method in payment_methods['data']['methods']:
        traders = requests.get(
            'https://localbitcoins.net/%s-bitcoins-online/%s/%s/.json' % (type_of_order, currency, method)).json()

        print 'Checking "%s" category...' % method

        for trader in traders['data']['ad_list']:
            bank_name = trader['data']['bank_name']

            for name in name_of_banks:
                if bank_name.lower().find(name) != -1:
                    print '---------\nUsername: %s\nFeedback Score: %s\nBank name: %s\nPrice: %s\nLink: %s\n---------' % (
                        trader['data']['profile']['username'], trader['data']['profile']['feedback_score'],
                        trader['data']['bank_name'], trader['data']['temp_price_usd'], trader['actions']['public_view'])
                    break


if __name__ == '__main__':
    search(sys.argv)
