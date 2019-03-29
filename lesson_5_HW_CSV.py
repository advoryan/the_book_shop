''' Источник данных - итоговые: баланс и отчет о прибылях и убытках по банкам РБ
'''

db_head = dict()                                    # Финальный словарь для причесанного csv
# Вспомогательные словари
db_data = dict()
key1= dict()
key2 = dict()

with open("csv_file.csv", "r") as t:
    text = t.readlines()
lines_count = len(text)                             # Количество строк в файле
    
# Распознавание заголовков (СПИСОК ДАТ)
dates = text[0].split(";")
dates.pop(0).pop()                                        # Убираем название
# dates.pop()                                         # Убираем \n
count_dates = len(dates)                            # Количество дат в строке

# Парсинг. Собираем в словарь: {cтатья:{дата:сумма}}
for ind in range(lines_count):
    if ind != 0:
        tmp = text[ind].split(";")
        for d in range(count_dates):
            dn = d + 1
            db_data[dates[d]] = tmp[dn]
        db_head[tmp[0]] = db_data.copy()

print(db_head)                                      # Выводим словарь для просмотра

# Выбираем __статью__ по номеру
ii = 1
for key in db_head:
    print(str(ii) + ".", key)
    key1[ii] = key
    ii += 1
# ii -= 1
name = int(input("\nВыберите порядковый номер статьи: "))

# Выбираем __дату__ по номеру
ii = 1
for i in range(count_dates):
    print(str(i +1 ) + ".", dates[i])
    key2[ii] = dates[i]
    ii += 1
date = int(input("\nВыберите дату (по номеру): "))

# Выводим результат запроса парсеру
print("\nОстаток по статье \"" + str(key1[name]) + "\" по состоянию на " +
    str(key2[date]) + " составляет: " + str(db_head[key1[name]][key2[date]]) + 
    " тыс.BYN")
