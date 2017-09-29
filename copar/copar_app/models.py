from django.db import models
from django.utils import timezone
# Create your models here.

class Questionnaire(models.Model):
    cpf_cnpj = models.CharField(max_length=14, null = False, unique=True)
    name = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.name
