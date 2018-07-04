# restfullECB


Is Django based project to share programatically several currency exchange rates in relation to EURO as a base currency (exchange rate 1).


## Quickstart

Clone repository to you local mahine:

```git clone https://github.com/mdyzma/restfullecb.git```

### Virtualenv

One may create virtual environment and run app there. `virtualenv` package must be present in the system, or user python interpreter

```virtualenv ~/.restfullecb```
```source .restfullecb/bin/activate```

After creating and activating local python, please instakll requitements to run application.

### Requirements

To install requirements cd to the copied project folder and enter command:

```pip install -r requirements.txt```

### Run app

Running application locally is easy as:

```python manage.py runserver```

# Description


Programm on start scrapps current ECB daily statistics and places them in data base. While running it will repeate this procedure every day from Monday to Friday.

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

For now API consists of single GET endpinttructed

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

1. test scrapper
2. test REST JSON view
3. Extend API with  PUT and DELETE
4. list view of most current record
5. refactor moel for more extensible (curencies table and ratestable with currency as a foreign key)
