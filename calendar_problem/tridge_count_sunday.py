def count_sundays():
    sunday_count = 0
    day = 2
    for year in range(1901, 2001):
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                days_in_month = 30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    days_in_month = 29
                else:
                    days_in_month = 28
            else:
                days_in_month = 31

            if day == 0:
                sunday_count += 1
            day = (day + days_in_month) % 7
    return sunday_count


print(count_sundays())
