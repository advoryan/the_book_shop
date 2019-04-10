# ------------------- GET OR CREATE --------------------

# obj, created = Series.objects.get_or_create( # obj - объект прилетел или создан
#     name="dfssdffdsf"
#     defaults=({"description": "11111111111")},
# )

utils.py

from data.models import Author

def create_series(obj): # функция создания серии
    aut = Author(
        name=obj["name"],
        # description=obj["description"] - не работает
)
    aut.save()