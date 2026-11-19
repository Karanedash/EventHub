from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField("Название", max_length=50)
    short_description = models.CharField("Краткое описание", max_length=200)
    description = models.CharField("Описание", max_length=500)
    date = models.DateTimeField("Дата и время проведения")
    location = models.CharField("Место проведения", max_length=100)
    image = models.ImageField("Изображение", upload_to="events/", blank=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    capacity = models.PositiveIntegerField("Вместимость")

    def __str__(self):
        return self.title