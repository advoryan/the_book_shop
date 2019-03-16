q = 0
db = dict() # Создаем словарь и заполняем для удобства
db = {
    'Саша':{
        'Возраст':33,
        'Пол':"м",
        'Вес':120,
        'Рост':185,
        'ИМТ':36,
        'Рекомендация':"У Вас большой избыточный вес! Рекомендуем обратиться к врачу!"},
    'Маша':{
        'Возраст':25,
        'Пол':"ж",
        'Вес':60,
        'Рост':172,
        'ИМТ':20,
        'Рекомендация':"Вы в хорошей форме! Так держать!"}
}

''' Берем все в цикл для удержания в памяти
введенных значений

'''
# Главное меню
def main_menu():
    global select
    print(
        "\nМеню калькулятора BMI:\n",
        "1 - Вывести список пользователей (Сейчас:", str(len(db)) + ")\n",
        "2 - Добавить пользователя\n",
        "3 - Удалить пользователя\n",
        "4 - Выбрать пользователя\n",
        "5 - Выход")
    select = int(input("Выберите пункт меню (1-4): ",))
    print("\n")
    return select

# Запрос параметров пользователя
def add_user():
    if select == 2:
        name = input("Введите имя: ")
        age = int(input("Количество полных лет?: "))
        sex = input("Выберите пол (рус. \"м\" - мужского, \"ж\" - женского): ")
        height = float(input("Рост в см: "))
        weight = float(input("Вес в кг: "))
        bmi = weight / ((height / 100) ** 2)

        # Отрисовка шкалы символами + обработка возможных ошибок
        if round(bmi, 0) > 40:
            for x in range(39):
                print(chr(9619), end="")
            print(chr(9608), end="")
            print(" Ваш ИМТ =", round(bmi, 2), end="")
        elif round(bmi, 0) <= 5:
            for x in range(40):
                print(chr(9617), end="")
            print(" Ошибка в данных! ИМТ =", round(bmi, 2), end="")
        else:
            for x in range(int(round(bmi, 0)) - 1):
                print(chr(9619), end="")
            print(chr(9608), end="")
            for x in range(40 - int(round(bmi, 0))):
                print(chr(9617), end="")
            print(" Ваш ИМТ =", round(bmi, 2), end="")

        # Библиотека рекомендаций
        grade1 = "Срочно поеште! Вы истощены!"
        grade2 = "Вы в хорошей форме! Так держать!"
        grade3 = "У Вас небольшой лишний вес, занятия спортом и легкая диета все исправят!"
        grade4 = "У Вас большой избыточный вес! Рекомендуем обратиться к врачу!"
        result = "Нет рекомендаций"

        # Оценка параметров польлзователся по шкале
        if age < 25:
            if sex == "м" or sex == "М":
                pass
            elif bmi < 18:
                result = grade1
            elif bmi >= 18 < 23:
                result = grade2
            elif 23 <= bmi < 27:
                result = grade3
            elif bmi >= 27:
                result = grade4
            if sex == "ж"or sex == "Ж":
                pass
            elif bmi < 16:
                result = grade1
            elif 16 <= bmi < 21:
                result = grade2
            elif 21 <= bmi < 26:
                result = grade3
            elif bmi >= 26:
                result = grade4

        if 25 <= age < 45:
            if sex == "м" or sex == "М":
                pass
            elif bmi < 20:
                result = grade1
            elif 20 <= bmi < 26:
                result = grade2
            elif 26 <= bmi < 31:
                result = grade3
            elif bmi >= 31:
                result = grade4
            if sex == "ж"or sex == "Ж":
                pass
            elif bmi < 18:
                result = grade1
            elif 18 <= bmi < 24:
                result = grade2
            elif 24 <= bmi < 29:
                result = grade3
            elif bmi >= 29:
                result = grade4

        if age >= 45:
            if sex == "м" or sex == "М":
                pass
            elif bmi < 22:
                result = grade1
            elif 22 <= bmi < 29:
                result = grade2
            elif 29 <= bmi < 34:
                result = grade3
            elif bmi >= 34:
                result = grade4
            if sex == "ж"or sex == "Ж":
                pass
            elif bmi < 20:
                result = grade1
            elif 20 <= bmi < 26:
                result = grade2
            elif 26 <= bmi < 32:
                result = grade3
            elif bmi >= 32:
                result = grade4

        # Занесение основных данных пользователя в справочник
        db[name] = {
            'Возраст':age,
            'Пол':sex,
            'Вес':round(weight,0),
            'Рост':height,
            'ИМТ':round(bmi, 0),
            'Рекомендация':result
            }




# Основной блок -------------------------------------------------------------------------

while q != 1:

    # Главное меню
selectt = main_menu()

if select = 2: add_user()    


    # Вывод списка пользователей
    if select == 1:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Список пользователей:")
        if len(db) == 0:
            print("Никого пока нет! Внесите пользователей!")
        ii = 1
        for key in db:
            print(str(ii) + ".", key)
            ii += 1
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Выбор пользователя (получение детальной информации)
    if select == 4:
        db_names = dict()
        if len(db) == 0:
            print("Никого пока нет! Внесите пользователей!\n")
        else:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            # Присваемаем число каждому пользователю число (чтобы не вводить имя а вызывать по числу)
            ii = 1
            for key in db:
                print(str(ii) + ".", key)
                db_names[ii] = key
                ii += 1
            ii -= 1
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("\n")
            n_user = input("Введите прядковый номер пользователя из списка: ")

            # Выводим инфо пользователя по номеру
            bmi1 = db[db_names[int(n_user)]]['ИМТ']
            print("\nИнформация по пользователю: [", (db_names[int(n_user)]),"]\n")
            for key, val in db[db_names[int(n_user)]].items():
                print(" - " + str(key) + ":", val)

                    # Отрисовка шкалы символами --------------------------------
            print("")
            if round(bmi1, 0) > 40:
                for x in range(39):
                    print(chr(9619), end="")
                print(chr(9608), end="")
                print(" ИМТ =", round(bmi1, 2), end="")
            elif round(bmi1, 0) <= 5:
                for x in range(40):
                    print(chr(9617), end="")
                print(" Ошибка в данных! ИМТ =", round(bmi1, 2), end="")
            else:
                for x in range(int(round(bmi1, 0)) - 1):
                    print(chr(9619), end="")
                print(chr(9608), end="")
                for x in range(40 - int(round(bmi1, 0))):
                    print(chr(9617), end="")
                print(" ИМТ =", round(bmi1, 2), end="")
            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Удаление выбранного пользователя
    if select == 3:
        db_names = dict()
        if len(db) == 0:
            print("Никого пока нет! Внесите пользователей для удаления!\n")
        else:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            # Присваемаем число каждому пользователю число (чтобы не вводить имя а вызывать по числу)
            ii = 1
            for key in db:
                print(str(ii) + ".", key)
                db_names[ii] = key
                ii += 1
            ii -= 1
            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("\n")
            n_user = int(input("Введите прядковый номер пользователя из списка для удаления: "))

            # Выводим инфо пользователя по номеру
            print("Для удаления выбран пользователь: [", db_names[n_user] ,"]")
            del_name = str(input("Удалить? (\"д\" - да / \"н\" - нет: "))
            a = ["д", "Д", "да", "Да"]
            if del_name in a:
                del (db[db_names[n_user]])
            print("")
    
    # Выход
    if select == 5:
        print("Всего хорошего!")
        q = 1
