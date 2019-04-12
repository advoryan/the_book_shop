from data.models import Series

def cs(obj1, obj2):
    sr = Series(name=obj1, description=obj2).save()
