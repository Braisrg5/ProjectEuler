'''https://projecteuler.net/problem=19
You are given the following information, but you may prefer to do
some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?


From now on, Sunday = 0, Monday = 1 and so on.
'''


def first_month_sundays(year, jan_first):
    '''Counts the number of Sundays that fell on the first of the month
    during a given year where the 1st of January is provided and also
    what day of the week is the 1st of January of the next year.
    '''
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[1] += 1

    first = jan_first
    sundays = 0
    for days in months:
        sundays += 0 + int(first == 0)
        first = (first + days) % 7
    return sundays, first


def sundays_twentieth_century():
    '''Counts the number of Sundays that fell on the first of the month
    during the twentieth century (1 Jan 1901 to 31 Dec 2000).'''
    jan_first = first_month_sundays(1900, 1)[1]
    sundays = 0
    for year in range(1901, 2001):
        n, jan_first = first_month_sundays(year, jan_first)
        sundays += n
    return sundays


if __name__ == '__main__':
    print(sundays_twentieth_century())  # 171, 0.0003s
