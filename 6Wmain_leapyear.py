
year=raw_input("input year example 1994:")
year=int(year)
if (year%4 == 0) and (year%100 !=0 or year%400==0):
    print "leap year"
else:
    print "normal year"