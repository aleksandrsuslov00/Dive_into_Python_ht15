# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime


current_datetime = datetime.now()

formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

day_of_week = current_datetime.strftime('%A')
week_number = current_datetime.isocalendar()[1]

formatted_datetime, day_of_week, week_number


print(f'Current date and time: {formatted_datetime}')
print(f'Day of the week: {day_of_week}')
print(f'Week number: {week_number}')

