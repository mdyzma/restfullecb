# restfullECB


Is Django based project to share programatically several currency exchange rates in relation to EURO as a base currency (exchange rate 1).


## Quickstart


## Description


Programm on start scrapps current ECB daily statistics and places them in data base.

List of currencies supported:

*USD
*JPY
*BGN
*CZK
*DKK
*GBP
*HUF
*LTL
*LVL
*PLN
*RON
*SEK
*CHF
*NOK
*HRK
*RUB
*TRY
*AUD
*BRL
*CAD
*CNY
*HKD
*IDR
*ILS
*INR
*KRW
*MXN
*MYR
*NZD
*PHP
*SGD
*THB
*ZAR

## API design

For now API is constructed

## API use

API to present collected data is simple and allows to send GET requiest for the table with all currences or speciffic item. 


Exemplary request:

    ```curl -X GET :0/currency/usd/
    ```

Should return:

    ```
    {
        <!-- some JSON TBD -->
    }

    ```

# TODO list

