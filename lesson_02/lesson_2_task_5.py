def month_to_season(month):
    if month == 12 or month == 1 or month == 2:
        season = "Зима"
        return season
    elif month == 3 or month == 4 or month == 5:
        season = "Весна"
        return season
    elif month == 6 or month == 7 or month == 8:
        season = "Лето"
        return season
    elif month == 9 or month == 10 or month == 11:
        season = "Осень"
        return season
    else:
        error = "Месяц должен быть от 1 до 12"
        return error
        

    
result = month_to_season(12)
print(result)
