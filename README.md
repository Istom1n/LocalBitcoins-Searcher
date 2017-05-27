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
---------
Processed 1.3%
Processed 2.6%
...
Processed 23.38%
Processed 24.68%
---------
Username: mostafaabdou
Feedback Score: 0
Bank name: advcash
Price: 2278.88 USD
Min - Max: 500 - 2000
Link: https://localbitcoins.net/ad/453764
---------
Processed 25.97%
Processed 27.27%
...
Processed 64.94%
Processed 66.23%
---------
Username: BTC_SAUDI_ARABIA
Feedback Score: 100
Bank name: Advcash
Price: 2183.83 USD
Min - Max: 100 - 1000
Link: https://localbitcoins.net/ad/436083
---------
Processed 67.53%
Processed 68.83%
...
Processed 98.7%
Processed 100.0%
```