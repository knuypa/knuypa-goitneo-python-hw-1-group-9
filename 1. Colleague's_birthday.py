from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays = defaultdict(list)

    for user in users: 
        name = user["name"]
        birthday_this_year = user["birthday"].replace(year=today.year).date()
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7: 
            day_of_week = weekdays[birthday_this_year.weekday()]
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)
            
    for day in weekdays[:5]:
        if birthdays[day]:
            print (f"{day}: {', '.join(birthdays[day])}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Roman Gubov", "birthday": datetime(1983, 11, 17)},
    {"name": "Evgenia Kniupa", "birthday": datetime(1992, 7, 24)},
]

get_birthdays_per_week(users)
