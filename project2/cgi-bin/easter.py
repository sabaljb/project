#!/usr/bin/env python3
import cgi
import calendar
from datetime import datetime , timedelta

def calculate_easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * 1 ) // 451
    month = (h + 1 - 7 * m + 114) // 31
    day = ((h + 1 - 7 * m + 114) % 31) + 1
    return datetime(year, month, day)

def format_date(date, numeric=True, verbose=False):
    if numeric and verbose:
        return f"{date.strftime('%d/%m/%Y')} ({date.strftime('%d%S')} {calendar.month_name[date.month]} {date.year})"
    elif numeric:
        return date.strftime('%d/%m/%Y')
    elif verbose:
        day_str = f"{date.strftime('%d%S')}"
        if day_str.endswith(('11','12','13',)):
            suffix = 'th'
        else:
            suffix = {'1': 'st', '2': 'nd', '3': 'rd'}.get(day_str[-1], 'th')
            return f"{date.strftime('%d')}{suffix} {calendar.month_name[date.month]} {date.year}"

def main():
    form = cgi.FieldStorage()


    if 'year' in form and form['year'].value:
        year = int(form.getvalue('year'))
    else:
        raise ValueError("Year is required.")

    format_option = form.getvalue('format')

    easter_date = calculate_easter_date(year)
    formatted_date = format_date(easter_date,
                                 numeric=format_option in ['numeric', 'both'],
                                 verbose=format_option in ['verbose', 'both'])

    
    print("""Content-type: text/html\n
    <html><title>Easter Date</title>
    <head>
    <link rel="stylesheet" type="text/css" href="../style.css">
    </head>
    <h2>Easter Date for {year}</h2>")
    <p>{formatted_date}</p>
    </body></html>""")

if __name__ == '__main__':
    main()

     

