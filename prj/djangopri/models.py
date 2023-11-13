from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True, editable=True) # description - описание |
                                              # null позваляет сохранить значене нан |
                                              # blank позволяет не заполнять значение |
                                              №№№ editable 32:28 №№№

    # Функция "__str__"
    def __str__(self):
        return self.name

    # Переписываем Categorys
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
