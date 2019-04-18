# ------------------- GET OR CREATE --------------------
#  created = Series.cts.get_or_create( # - объект прилетел или создан
#     name="dfssdffdsf"
#     defaults=({"description": "11111111111")},# )

from django.db import models
from data.models import *
from books.models import *

# 1. принимают на вход все необходимые данные

# 2. Функция, которая создает объекты справочников (автор, серия....)  в базе данных
def cr_author(obj1, obj2, obj3): crauthor = Author(first_name=obj1, last_name=obj2, country=obj3).save()
def cr_genre(obj1): crgenre = Genre(name=obj1).save()
def cr_series(obj1, obj2): crseries = Series(name=obj1, description=obj2).save()
def cr_publish(obj1, obj2, obj3): crpublish = Publish(name=obj1, country=obj2, city=obj3).save()
def cr_binding(obj1): crbinding = Binding(name=obj1).save()
def cr_bookformat(obj1): crbookformat = BookFormat(name=obj1).save()

# 3. удаляет определенный объект в БД
def delfunc(fc_name, pk_key):
    print(fc_name)
    fc_name.objects.get(pk=pk_key).delete()

# 4. Считает кол-во объектов в таблице - например кол-во авторов в справочнике авторы
def obj_count1():
    objcount1 = Author.objects.all()
    print (len(objcount1))

# 5. Написать скрипт, который наполняет таблицы справочником большим кол-вом объектов
def create_data():
    a_list = []
    for i in range(1, 100):
        obj = Genre(name='Жанр ' + i)
        a_list.append(obj)
    Genre.objects.bulk_create(a_list)

# 6. Функция, выдающая кол-во авторов в справочние, чье имя начинается в переданного параматра (например Пуш)
def count_data(table_name):
    data = table_name.objects.count()

# 7. Функция, которая принимает на вход словарь со всеми значениями, необходимыми для создания книги,
# а это данные самой книги и данные справочников и создает ее в бд со всеми справочниками

def create_book(bk):
    obj = Book(
        name=bk['name'],
        price=bk['price'],
        year=bk['year'],
        page=bk['page'],
        isbn=bk['isbn'],
        weight=bk['weight'],
        age_limit=bk['age_limit'],
        book_amount=bk['amount'],
        available=bk['available'],
        rate=bk['rate'])
    obj.serie = Series.objects.get(name=bk['serie_name'])
    obj.bind = Binding.objects.get(binding_type=bk['type'])
    obj.book_format = BookFormat.objects.get(pk=bk['size_pk'])
    obj.publish = Publish.objects.get(name=bk['publish_name'])
    obj.save()
    aut  = Author.objects.get(pk=bk['author_pk'])
    genr = Genre.objects.get(name=bk['genre_name'])
    obj.author.add(aut)
    obj.genre.add(genr)

    new_book = {
        'name': 'Книга',
        'price': 100,
        'year': 1960,
        'page': 800,
        'isbn': '11111111',
        'weight': 400,
        'age_limit': 16,
        'amount': 8,
        'available': True,
        'rate': 7,
        'serie_name': '11111',
        'type': 'Твердая обложка',
        'size_pk': 11,
        'publish_name': 'Hom Inc.',
        'author_pk': 3,
        'genre_name': 'Детектив'}

# 8. Функция, которая принимает значения для (какого-то) справочника, проверяет его наличие в БД по основному полю,
# если такая запись есть - обновляет ее, если нет - создает. Реализовать штатным способом Джанго
def upd_or_cr(name):
    obj. created = Series.objects.update_or_create(name=name)
    
# 9. Функцию, выводящую список всех книг данного автора, сериии... (справочник на выбор)

def books_list(book_name, key):
    obj = book_name.objects.get(pk=key)
    for i in obj.books.all():
        print(i)