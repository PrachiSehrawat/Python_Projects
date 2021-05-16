###################### CALENDER ##########################

import calendar

usr_y = int(input("Enter The Year: "))
usr_m = int(input("Enter The Month: "))
print(calendar.month(usr_y, usr_m))


############# To Check if Year is a Leap Year or Not ##############

year = int(input("Enter The Year: "))

if (year%4) == 0:
    if (year%100) == 0:
        if (year%400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))



