import datetime

date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
print(f'Полное название месяца: {python_date.strftime('%B')}')
print(f'Дата в другом формате: {python_date.strftime('%d.%m.%Y, %H:%M')}')
