import time

month_names = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "dicember": 12,
}


def casteable(q):
    try:
        int(q)
        return True
    except ValueError:
        return False


settime = input("write the actual time like in 24h format , like this 16:00")
if len(settime) < 4 or len(settime) >= 6:
    print("that is not a time format)")
    exit()
if any(char.isalpha() for char in settime):
    print("that is not a time format")
    exit()
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
month = 0
year = 0
x = 1
while x == 1:
    realtime = input("want to place an actual time? , y/n")
    if realtime[0] == "y":
        year = input("write the year")
        if not (casteable(year)):
            print("that is not a year")
            exit()
        if int(year) % 4 == 0:
            year_days = 366
        else:
            year_days = 365
        month_names = {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "dicember": 12,
        }
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year_days == 366:
            month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(year)
        month = input("write the month")

        if month in month_names:
            month = month_names[month]
        elif not (casteable(month)):
            print("that is not a month")
            exit()
        month = int(month)
        if not (month > 0 and month <= 12):
            print("that is not a month")
            exit()
        day = int(input("write the day"))
        if not (casteable(day)):
            print("that is not a day")
            exit()
        if not (0 < day <= month_days[month - 1]):
            print("that is not a real day")
            exit()
        x = 2
    elif realtime[0] == "n":
        x = 2
    else:
        print("please write y or n")
        x = 1


writestart = input("Write something to start the clock")

Minutes = int(Minutes)

Hours = int(Hours)
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
                if day >= month_days[month - 1]:
                    day = 0
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
            month,
            "month of",
            year,
        )
    elif month >= 1:
        print(
            "time:",
            Hours,
            "hours:",
            Minutes,
            "minutes of",
            day,
            "day of",
            "month of",
            month,
            "h",
        )
    elif day >= 1:
        print("time:", Hours, "hours:", Minutes, "minutes of", day, "h")
    else:
        print("time:", Hours, "hours:", Minutes, "h and", Isecond, "seconds")
# if settime[]


# timesets=('1:)
