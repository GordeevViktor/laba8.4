import datetime as dt

start_time = dt.datetime(2011, 4, 17)  # дата выхода первой серии
final_time = dt.datetime(2019, 4, 15)  # впишите дату выхода последней серии
    
duration = final_time - start_time  # вычислите, сколько времени шёл сериал
    
print(duration)