temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31,
                33, 31, 30, 32, 30, 28, 24, 23]
high_temperatures = list(filter(lambda temp: temp > 28, temperatures))
print(f'Самая высокая температура: {max(high_temperatures)}')
print(f'Самая низкая температура: {min(high_temperatures)}')
print(f'Средняя температура: {round(sum(high_temperatures) / len(high_temperatures), 2)}')
