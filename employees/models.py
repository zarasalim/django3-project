from pathlib import Path

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    gender = models.CharField(
        max_length=20,
        verbose_name='Пол'
    )
    skills = models.TextField(
        verbose_name='Навыки'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EmployeeImage(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Сотрудник'
    )
    image = models.ImageField(
        upload_to='employees/',
        verbose_name='Фотография'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядковый номер'
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.employee} — фото {self.order}'


@receiver(post_delete, sender=EmployeeImage)
def delete_employee_image(sender, instance, **kwargs):
    if instance.image:
        image_path = Path(instance.image.path)

        if image_path.exists():
            image_path.unlink()