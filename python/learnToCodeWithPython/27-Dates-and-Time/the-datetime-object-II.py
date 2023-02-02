# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime
# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)
# one_from_two(some_date, some_time) => datetime object representing 
# 2002-02-22 09:45:23

from datetime import date, time, datetime

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)


def algorithm(algorithm_some_date: date, algorithm_some_time: time) -> None:
    def one_from_two(input_some_date: date, input_some_time: time) -> datetime:
        value = datetime(input_some_date.year, input_some_date.month, input_some_date.day, input_some_time.hour,
                         input_some_time.minute, input_some_time.second)
        return value

    print("The combination of date and time is ", one_from_two(algorithm_some_date, algorithm_some_time))


algorithm(some_date, some_time)
