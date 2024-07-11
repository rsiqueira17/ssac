# conversao de padroes de data e valores
from datetime import datetime


def set_current_date_ptbr():
    return datetime.now().today().strftime('%d/%m/%Y') #f"{day}/{month}/{year}"


def set_date_ptbr(date):
    #day, month, year = str(datetime.now().today()).split('-')[::-1]
    #day = day.zfill(2)
    #month = month.zfill(2)

    return '/'.join(str(date).split('-')[::-1])


def set_currency_ptbr(value):
    return f'{float(value):.2f}'.replace('.', ',')


def set_currency_us(value):
    return float(f'{value}'.replace('.', '').replace(',', '.'))


def format_value_ptbr(value):
    format_value = ''
    value = value.replace(',', '').replace('.','')[:11]
    count = len(value)

    for index in range(count):
        if not value[index] in "0123456789": continue

        if index in [count - 3]:
            format_value += value[index] + ","
        elif index in [count - 6, count - 9]:
            format_value += value[index] + "."
        else: 
            format_value += value[index]

    return format_value


def format_cpf(value):
    format_value = ''
    value = value.replace('-', '').replace('.','')[:11]
    count = len(value)

    for index in range(count):
        if not value[index] in "0123456789": continue

        if index in [count - 3]:
            format_value += value[index] + "-"
        elif index in [count - 6, count - 9]:
            format_value += value[index] + "."
        else: 
            format_value += value[index]

    return format_value