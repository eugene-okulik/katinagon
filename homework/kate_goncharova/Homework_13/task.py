import datetime
import os

base_path = os.path.dirname(__file__)
eugene_file_path = os.path.join(os.path.dirname(os.path.dirname(base_path)), 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_file_path) as eugene_file:
        for line in eugene_file.readlines():
            new_list = line.split()[:3]
            new_list[1:] = [' '.join(new_list[1:])]
            yield new_list


for data_line in read_file():
    if data_line[0] == '1.':
        date_time_obj = datetime.datetime.strptime(data_line[1], '%Y-%m-%d %H:%M:%S.%f')
        print(date_time_obj + datetime.timedelta(days=7))
    elif data_line[0] == '2.':
        date_time_obj = datetime.datetime.strptime(data_line[1], '%Y-%m-%d %H:%M:%S.%f')
        print(date_time_obj.strftime('%A'))
    elif data_line[0] == '3.':
        date_time_obj = datetime.datetime.strptime(data_line[1], '%Y-%m-%d %H:%M:%S.%f')
        print((datetime.datetime.now() - date_time_obj).days)
