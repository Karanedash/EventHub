from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.DateTimeField("Дата и время проведения")
    location = models.CharField(max_length=100)

    is_published = models.BooleanField("Опубликовано", default=False)
    capacity = models.PositiveIntegerField("Вместимость")
