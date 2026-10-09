from django.db import models

from employees.models import Employee


class Workplace(models.Model):
    desk_number = models.PositiveIntegerField(
        verbose_name="Номер стола",
    )

    additional_information = models.TextField(
        blank=True,
        verbose_name="Дополнительная информация",
    )

    employee = models.OneToOneField(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Сотрудник",
    )

    def __str__(self):
        return f"Рабочее место №{self.desk_number}"
