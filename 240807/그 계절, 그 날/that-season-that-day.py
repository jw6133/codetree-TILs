y,m,d=map(int,input().split(" "))

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"

def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day > days_in_month[month - 1]:
        return False

    return True


def check_date(y, m, d):
    if is_valid_date(y, m, d):
        print(get_season(m))
    else:
        print(-1)

check_date(y,m,d)