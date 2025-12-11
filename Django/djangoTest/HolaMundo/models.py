from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField (verbose_name = "Nombre",
                             max_length = 100,
                             default = '')
    lastname = models.CharField(verbose_name = "Apellidos",
                                max_length = 150,
                                default = '')
    age = models.PositiveSmallIntegerField (verbose_name = 'Edad')