# LocalBitcoins Searcher

This script written to search for sellers of international payment systems (which is not available on the website).

## How to use this?
Just clone a repository and write:

    python search_exchange.py [sell/buy] [currency] [list of banks...]

Example:

    python search_exchange.py sell USD advcash advancedcash advanced

and you get...

```
Type of order: sell
Currency: USD
Banks List: ['advcash', 'advancedcash', 'advanced']
Checking "alipay" category...
Checking "other-pre-paid-debit-card" category...
Checking "other-online-wallet" category...
---------
Username: mostafaabdou
Feedback Score: 0
Bank name: advcash
Price: 1600.66
Link: https://localbitcoins.net/ad/453764
---------
Checking "sepa-eu-bank-transfer" category...
Checking "easypaisa" category...
Checking "webmoney" category...
Checking "paypal" category...
Checking "transferwise" category...
Checking "other-online-wallet-global" category...
---------
Username: yura023
Feedback Score: 100
Bank name: Advanced Cash
Price: 1512.62
Link: https://localbitcoins.net/ad/437758
---------
Checking "cash-deposit" category...
Checking "ebay-gift-card-code" category...

```