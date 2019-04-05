from django.db import models

class Serie(models.Model):
    name = models.CharField("Серия", max_length=20) # Название колонки, можно ли быть пустым для БД, то же для валюдаторов джанго и макс длинна
    description = models.TextField("Описание", max_length=2000) # Нет ограничения по длинне и подефолтных
    def __str__(self):
        return self.name

class Genre(models.Model):
    GENRE_CH = (
        ('Ф', 'Фантастика'),
        ('Д', 'Детективы'),
        ('Р', 'Рассказ'),
        ('Б', 'Биография'),
        ('У', 'Учебные материалы'),
        ('М', 'Манга')
    )
    genre_type = models.CharField("Название жанра", max_length=1, choices=GENRE_CH)
    genre_description = models.CharField("Описание жанра", max_length=300)

class Author(models.Model):
    author_first_name = models.CharField("Имя автора", max_length=80)
    author_last_name = models.CharField("Фамилия автора", max_length=80)
    author_country = models.CharField("Страна", max_length=80)

class Publisher(models.Model):
    publisher_name = models.CharField("Имя автора", max_length=80)
    publisher_adress = models.CharField("Фамилия автора", max_length=80)
    publisher_country = models.CharField("Страна", max_length=80)

class Meta:
    ordering = ["name"] # сортировка по имени
    verobose_name = "Серии" 
    verobose_name_plural = "Серии" 


# 
