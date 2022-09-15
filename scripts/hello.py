#!/usr/bin/env python3
from datetime import datetime
from dev_aberto import hello
import gettext
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number, format_decimal, format_percent, format_currency
if __name__ == '__main__':
    gettext.install('cli', localedir='locale') 
    date, name = hello()
    date = datetime(int(date[:4]),int(date[5:7]),int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
    print(date)
    date = format_date(date)
    print(_('Último commit feito em:'), _(date), _(' por'), name)
