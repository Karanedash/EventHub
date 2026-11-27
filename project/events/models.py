from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField("Название", max_length=50)
    short_description = models.TextField("Краткое описание")
    description = models.TextField("Описание")
    date = models.DateTimeField("Дата и время проведения")
    location = models.CharField("Место проведения", max_length=100)
    image = models.ImageField("Изображение", upload_to="events/", blank=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    capacity = models.PositiveIntegerField("Вместимость", blank=True, null=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")
    name = models.CharField("Имя", max_length=20)
    email = models.EmailField("Email")
    phone = models.CharField("Номер телефона", max_length=12, blank=True)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата создания", default=timezone.now)

    status_choises = [("new", "Новая"), ("confirmed", "Подтверждена"), ("cancelled", "Отменена")]
    status = models.CharField("Статус заявки", max_length=20, choices=status_choises, default="new")

    def __str__(self):
        return f"Запись на мероприятие {self.event.title}"


class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=20)
    email = models.CharField("Email", max_length=25)
    message = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата создания")