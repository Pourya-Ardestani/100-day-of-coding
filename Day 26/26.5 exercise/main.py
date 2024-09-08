weather_c = {
    "Monday": 12,
    "tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "sunday": 24,
}

weather_f = {day: degree*1.8+32 for (day, degree) in weather_c.items()}

print(weather_f)