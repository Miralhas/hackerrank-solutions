import calendar
# (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)
weekdays = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}
month, day, year = input().split()


if month[0] == "0":
    month = month[1:]

if day[0] == "0":
    day = day[1:]


dia = calendar.weekday(int(year), int(month), int(day))

print(weekdays[dia])