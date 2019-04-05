# from django.db import models

# # Create your models here.
# # Lesson 8 !!!!!!!!!!!!!!!
# # ТУТ РАБОТАЕМ С БД !!!!!!!!! <<<<<<<<<<<<<<<<<<<<

# # 1) python manage.py startapp refs

# # Класс, описысвает ТАБЛИЦУ по сериям
# # Появляется PK  -  id = models.AutoField - primary key для каждого класса (таблицы) по дефолту делает Django
# # Model - встроена
# # Описывем поля (колонки)

# class Serie(models.Model):
#     name = models.CharField("Серия", max_length=20) # Название колонки, можно ли быть пустым для БД, то же для валюдаторов джанго и макс длинна
# # null и blanck по дефолту False
#     description = models.TextField("Описание", max_length=2000) # Нет ограничения по длинне и подефолтных

# # Когда на печать:
#     def __str__(self):
#         return self.name + "_"
# # 2) make migrations
# # 3) migrate

# # class Genre(models.Model):
# #     GENRE_CH = (
# #         ('Фантастика'),
# #         ('Детектив'),
# #         ('Биография'),
# #     )
# #     genre_name_field = models.CharField(max_length=60)
# #     genre_name = models.CharField(max_length=60, choices=GENRE_CH)

# class Genre(models.Model):
#     GENRE_CH = (
#         ('Ф', 'Фантастика'),
#         ('Д', 'Детективы'),
#         ('Р', 'Рассказ'),
#         ('Б', 'Биография'),
#         ('У', 'Учебные материалы'),
#         ('М', 'Манга')
#     )
#     shirt_size = models.CharField("Жанр", max_length=1, choices=GENRE_CH)

# class Authors(models.Model):
#     genre_type = models.CharField("Название жанра", max_length=1, choices=GENRE_CH)
#     genre_description = models.CharField("Описание жанра")

# class Meta:
#     ordering = ["name"] # сортировка по имени
#     verobose_name = "Серии" 
#     verobose_name_plural = "Серии" 


# # 
