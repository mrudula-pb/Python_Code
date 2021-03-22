###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    # YOUR CODE HERE
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

    '''
        if daysInMonth(year, month) == 30:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
    '''

def dateIsBefore(year1, month1, day1, year2, month2, day2):

    if year1 < year2:
        return True
    else:
        if year1 == year2:
            if month1 < month2:
                return True
            else:
                if month1 == month2:
                    if day1 < day2:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    #assert not dateIsBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def daysInMonth(year, month):
    if year != isLeapYear(year) or year == isLeapYear(year):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        else:
            if month == 2:
                if isLeapYear(year):
                    return 29
                else:
                    return 28
            return 30

def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                #print("{0} is a leap year".format(year))
                return True
            else:
                #print("{0} is not a leap year".format(year))
                return False
        else:
            #print("{0} is a leap year".format(year))
            return True
    else:
        #print("{0} is not a leap year".format(year))
        return False

def main():

    # value = dateIsBefore(2012, 4, 30, 2012, 6, 30)
    # print(value)

    value1 = daysBetweenDates(2013, 1, 24, 2013, 6, 29)
    print(value1)

    # days_Month = daysInMonth(1912, 12)
    # print(days_Month)

    #isLeapYear(2015)

    # year, month, day = nextDay(2012, 2, 28)
    # print("Year: " + str(year) + ", Month: " + str(month) + ", Day: " + str(day))

    '''
    year, month, day = nextDay(2012, 1, 30)
    print("Year: " + str(year) + ", Month: " + str(month) + ", Day: " + str(day))

    year, month, day = nextDay(2012, 12, 30)
    print("Year: " + str(year) + ", Month: " + str(month) + ", Day: " + str(day))
    '''

if __name__ == '__main__':
    main()