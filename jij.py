import time

settime = input("write the actual time like in 24h format , like this 16:00")
if settime[1] == ":":

    if int(settime[3]) > 60:
        print("error , minute dos not exist")
        exit()

    Hours = settime[0]
    Minutes = settime[2] + settime[3]
else:
    if int(settime[4]) > 60:
        print("error , minute dos not exist")
        exit()
    if int(settime[0] + settime[1]) > 24:
        print("error , hour dos not exist")
        exit()
    Hours = settime[0] + settime[1]
    Minutes = settime[3] + settime[4]
print(Hours)
Isecond = 0
day = 0
week = 0
month = 0
year = 0
x = 1
realtime=input('want to place an actual time? , y/n')
if realtime[0] == "y":
    day=input('write the day of the week')
    daysofweek={'monday' : 1 , 'tuesday' : 2 , 'wednesday' : 3 , 'thursday' : 4 ,'friday' : 5 , 'saturday' : 6 , 'sunday' : 7}
    day=day[daysofweek[day]]
    week=input('write the week')
    week=int(week)
    month=input('write the month')
    month=int(month)
    year=input('write the year')
    year=int(year)
writestart = input("Write something to start the clock")
Minutes=int(Minutes)
Hours=int(Hours)
while True:
    time.sleep(1)
    Isecond = Isecond + 1

    if Isecond >= 60:
        Isecond = 0
        Minutes = Minutes + 1
        if Minutes >= 60:
            Minutes = 0
            Hours = Hours + 1
            if Hours >= 24:
                Hours = 0
                day = day + 1
                if day >= 7:
                    day = 0
                    week = week + 1
                    if week >= 7:
                        week = 0
                        month = month + 1
                        if month >= 12:
                            month = 0
                            year = year + 1
    if year >= 1:
        print(
            "time:",
            Hours,
            "hours:",
            Minutes,
            "minutes of",
            day,
            "day of",
            week,
            "week of",
            month,
            "month of",
            year,
        )
    else:
        if month >= 1:
            print("time:", Hours, "hours:", Minutes, "minutes of", day, "day of", week, "month of", month, "h")
        else:
            if week >= 1:
                print("time:", Hours, "hours:", Minutes, "minutes of", day, "day of", week, "h")
            else:
                if day >= 1:
                    print("time:", Hours, "hours:", Minutes, "minutes of", day, "h")
                else:
                    print("time:", Hours, "hours:", Minutes, "h and",Isecond,'seconds')
    if int(Hours) <1:
        x=x-1
# if settime[]


# timesets=('1:)
