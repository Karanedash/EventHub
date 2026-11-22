from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField("Название", max_length=50)
    short_description = models.TextField("Краткое описание")
    description = models.TextField("Описание")
    date = models.DateTimeField("Дата и время проведения")
    location = models.CharField("Место проведения", max_length=100)
    image = models.ImageField("Изображение", upload_to="events/", blank=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    capacity = models.PositiveIntegerField("Вместимость", blank=True)

    def __str__(self):
        return self.title