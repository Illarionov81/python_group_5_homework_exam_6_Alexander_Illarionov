from django.db import models

DEFAULT_CATEGORY = 'active'
STATUS_CHOICES = (
    (DEFAULT_CATEGORY, 'Активно'),
    ('blocked', 'Заблокировано'),
)


class GuestBook(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя Автора')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Емайл')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=14, verbose_name='Статус',
                              choices=STATUS_CHOICES, default=DEFAULT_CATEGORY)

    def __str__(self):
        return f'{self.name} - {self.text}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'