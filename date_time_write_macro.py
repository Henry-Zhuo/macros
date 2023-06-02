''' Collection of functions for formatting strings for date and time, and for
automated typing of said strings.
'''

from datetime import datetime
import keyboard


def get_date_and_time_string(time: datetime):
    ''' Returns the date and time for the given datetime, in the format
    "WEEKDAY MONTH DAY_OF_MONTH YEAR HH:MM:SS" in the 24 hour clock format.
    Ex: "Friday July 2 2023 14:53:01"
    '''
    time_string = get_time_string(time)
    date_string = get_date_string(time)
    date_and_time_string = f'{date_string} {time_string}'
    return date_and_time_string



def get_date_string(time: datetime):
    ''' Returns the date for the given datetime,
    in the format "WEEKDAY MONTH DAY_OF_MONTH YEAR"
    Ex: "Friday July 2 2023"
    '''
    # Remove padding 0 on left
    day_of_month_string = time.strftime('%d').lstrip('0')
    year_string = time.strftime('%Y').lstrip('0')
    date_string = time.strftime('%A %B ') + f'{day_of_month_string} {year_string}'
    return date_string



def get_time_string(time: datetime):
    ''' Returns the time of day for the given datetime, in the format
    "HH:MM:SS".
    Ex: "14:53:01"
    '''
    return time.strftime('%X')



def get_short_date_and_time(time: datetime):
    ''' Returns a string representing the given time in a shortened format, suitable for file names

    Ex: If given time is Sunday March 29 2022 9:18:25 pm, return "SunMar29_2022_21.18.25"
    '''
    short_day_of_week_and_month_string = time.strftime('%a%b')
    day_of_month_string = time.strftime('%d').lstrip('0')
    short_year_and_time_string = time.strftime('_%Y_%H.%M.%S')

    short_date_and_time_string = short_day_of_week_and_month_string \
                                + day_of_month_string \
                                + short_year_and_time_string
    return short_date_and_time_string



def write_date_and_time():
    ''' Sends keypresses to write out the date and time according to
    string returned by get_date_and_time_string().
    '''
    now = datetime.now()
    date_and_time_string = get_date_and_time_string(now)
    keyboard.write(date_and_time_string)



def write_time():
    ''' Sends keypresses to write out the time of day according to
    string returned by get_time_string().
    '''
    now = datetime.now()
    time_string = get_time_string(now)
    keyboard.write(time_string)



def write_date():
    ''' Sends keypresses to write out the date according to
    string returned by get_date_string().
    '''
    now = datetime.now()
    date_string = get_date_string(now)
    keyboard.write(date_string)



def write_short_date_and_time():
    ''' Sends keypresses to write out the date and time according to
    string returned by get_short_date_and_time().
    '''
    now = datetime.now()
    short_date_and_time_string = get_short_date_and_time(now)
    keyboard.write(short_date_and_time_string)



def write_end_time():
    ''' Sends keypresses to write out the time according to
    string returned by get_time_string(), prepended with " - ".
    '''
    now = datetime.now()
    time_string = get_time_string(now)
    end_time_string = ' - ' + time_string
    keyboard.write(end_time_string)



# Exports

macros = {
    's': write_date_and_time,
    't': write_time,
    'd': write_date,
    'p': write_short_date_and_time,
    'e': write_end_time,
}
