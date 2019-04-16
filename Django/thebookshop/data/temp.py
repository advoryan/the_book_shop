from data.models import *

# def cs(obj1, obj2):
#     sr = Series(name=obj1, description=obj2).save()

def get_books(aut):
    books  = aut.books.all()
    print(books.count())

a_list=[] -# BUlK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
for i in range(100_000):
    a_list.append(
        Series(
            name="name " + str(i),
            description="description " + str(i)
        ))
Series.objects.bulk_create(a_list)

# dupmdata
# python manage.py dupmdata data.Series - вывод всех данных
#./data/fixtures/series.json - в файл

# loaddata - загрузить
# python manage.py loaddata series.json - загрузка всех данных
