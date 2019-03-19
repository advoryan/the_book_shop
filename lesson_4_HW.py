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
        'Рекомендация':"Вы в хорошей форме! Так держать!"}}
log_db = {'a':"111", 'b':"222"}
log_status = False
import functools

# Главное меню
def main_menu():
    global select
    print(
        "\nМеню калькулятора BMI:\n",
        "Ваш log in статус: " + str(log_status) + "\n",
        "1 - Вывести список пользователей (Сейчас:", str(len(db)) + ")\n",
        "2 - Добавить пользователя\n",
        "3 - Удалить пользователя\n",
        "4 - Выбрать пользователя\n",
        "5 - ЗАЛОГИНЬТЕСЬ!!!!\n",
        "6 - ЗАРЕГИСТРИРУЙТЕСЬ\n",
        "7 - Выход")
    select = int(input("Выберите пункт меню (1-5): ",))
    print("\n")
    return select

# Проверка залогинен или нет (подготовка обертки)
def login_required(fn):
    global log_status
    def wrapper():
        print(log_status)
        if log_status == False:
            return log_in()
        else:
            return fn()
    return wrapper
            
# Только ввод логина и пароля ПЕРЕДЕЛАТЬ НА ВНЕСЕНИЕ ПАРОЛЯ
def log_in():
    global log_db
    global log_status
    log_name = str(input("Login: "))
    log_pass = str(input("Password: "))
    if log_name in log_db:
        if str(log_pass) != log_db[log_name]:
            print("Неверный пароль!!!")
        else:
            log_status = True
            print("Добро пожаловать,", str(log_name))
    else:
        print("Нет такого пользователя! Пожалуйста, зарегистрируйтесь!")
        # переход на регистрацию нового пользователя
    # return log_name, log_pass

# # ЗАМЫКАНИЕ ПРОВЕРКИ
# def checki(aaa):
#     def sel_function():
#         print(aaa)
#         if aaa == True:
#             if select == 1: show_user()
#             elif select == 2: add_user()
#             elif select == 3: del_user()
#             elif select == 4: detail_user()
#     return sel_function()

# Вывод списка пользователей
@login_required
def show_user():
    global select
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
    return select 

# Добавление пользователя
@login_required
def add_user():
    global select
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
        global db
        db[name] = {
            'Возраст':age,
            'Пол':sex,
            'Вес':round(weight,0),
            'Рост':height,
            'ИМТ':round(bmi, 0),
            'Рекомендация':result
            }

# Удаление выбранного пользователя
@login_required
def del_user():
    global db
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

# Выбор пользователя (получение детальной информации)
@login_required
def detail_user():
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

# Основной блок -------------------------------------------------------------------------
while True:

    main_menu()
    # sel_function()""
    # checki(login_check)
    
    
    if select == 1: show_user()
    elif select == 2: add_user()
    elif select == 3: del_user()
    elif select == 4: detail_user()

    if select == 5:
        log_in()
        # if log_status == False: log_status = True
        # else:
        #     if log_status == True: log_status = False

    # Выход
    if select == 7:
        print("Всего хорошего!")
        break
