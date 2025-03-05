'''https://projecteuler.net/problem=19
You are given the following information, but you may prefer to do some research
for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''


# Sunday = 0, Monday = 1, Tuesday = 2...
def first_month_sundays(year, jan_first):
    '''Counts the number of Sundays that fell on the first of the month during
    a given year where the 1st of January is provided and also what day of the
    week is the 1st of January of the next year.
    '''
    # Number of days of each month
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Adjust for leap years
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[1] += 1

    # The current day is the first of the year
    first_of_month = jan_first
    # And the number of sundays is 0 at the beginning of the year
    sundays = 0
    # For every month of the year
    for days in months:
        # We check if the first day is a Sunday
        sundays += 0 + int(first_of_month == 0)
        # Then, we sum the number of days of the month mod 7 (1*)
        first_of_month = (first_of_month + days) % 7
    return sundays, first_of_month


def sundays_twentieth_century():
    '''Counts the number of Sundays that fell on the first of the month during
    the twentieth century (1 Jan 1901 to 31 Dec 2000).'''
    # We first initialize the variable for the year 1901
    jan_first = first_month_sundays(1900, 1)[1]

    sundays = 0
    for year in range(1901, 2001):
        # For each year, we get the number of sundays that fell on the first of
        # the month and the first day of the next year
        n, jan_first = first_month_sundays(year, jan_first)
        sundays += n
    return sundays


if __name__ == '__main__':
    print(sundays_twentieth_century())  # 171, 0.0003s


'''
#-------#
# Notes #
#-------#

(1*)
If Sunday = 0, Monday = 1, Tuesday = 2... and we know that the first day of the
year 1901 is Monday, we can initialize the current day value to 1. After the
next month passes, the first day of february would be (1 + 31) mod 7, which is
3, so Wednesday. This way, if for the first day of any month, the value that
keeps track of the days is 0, we know it fell on a Sunday.
'''
