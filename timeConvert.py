total_seconds = int(input('введите количество секунд: '))
hours = total_seconds // 3600
minutes = total_seconds // 60
seconds = total_seconds % 60

print('Часов: ', hours)
print('Минут: ', minutes)
print('Секунд: ', seconds)
