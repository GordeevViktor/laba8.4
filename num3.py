# подключите библиотеку datetime под именем dt
import datetime as dt

start_moment = dt.datetime(2019, 11, 16, 12, 0)  # напишите код здесь
current_moment = dt.datetime(2019, 11, 21, 14, 50)  # напишите код здесь

total_time = current_moment - start_moment  # и здесь

print(total_time)