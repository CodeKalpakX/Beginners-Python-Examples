# We assume that given dates are correct
# and 
# solved for problem set in cs course on udacity.com
from calendar import isleap

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    dom = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    domleap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (isleap(year1) and isleap(year2)):
        e1 = sum(domleap) + sum(domleap[:month1 - 1]) + day1
        e2 = sum(domleap) + sum(domleap[:month2 - 1]) + day2
        return e2 - e1
    
    days = 0
    if isleap(year1):
        days += (sum(domleap[month1 - 1:]) - day1) + sum(dom[:month2 - 1]) + day2 
    elif isleap(year2):
        days += (sum(dom[month1 - 1:]) - day1) + sum(domleap[:month2 - 1]) + day2 
    else:
        days += (sum(dom[month1 - 1:]) - day1) + sum(dom[:month2 - 1]) + day2 
    for year in range(year1 + 1, year2):
        if isleap(year):
            days += sum(domleap)
        else:
            days += sum(dom)
    return days
    

date1=input("Enter a first date in YYYY-MM-DD format")
year1,month1,day1=map(int,date1.split('-'))

date2=input("Enter a second date in YYYY-MM-DD format")
year2,month2,day2=map(int,date2.split('-'))

days=daysBetweenDates(year1, month1, day1, year2, month2, day2)
print("Number of days between {} and {} is \n  {}".format(date1,date2,abs(days)))
