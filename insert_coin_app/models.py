from django.db import models
from decimal import Decimal
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class PS5(models.Model):
    SI = 'Si'
    NO = 'No'
    OPCIONES_ONLINE = [
        (True, SI),
        (False, NO),
    ]
    nombre= models.CharField(max_length=60)
    genero= models.CharField(max_length=15)
    online = models.BooleanField(choices=OPCIONES_ONLINE)
    precio= models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "PS5"
        verbose_name_plural = "PS5"

    @property
    def precio_con_simbolo(self):   #Es para que aparezca el símbolo euros adelante del precio.
        return f'€{self.precio}'

    def __str__(self):
        return f"{self.nombre}"
    


class XBOX_series_x(models.Model):
    nombre= models.CharField(max_length=60)
    genero= models.CharField(max_length=15)
    online= models.BooleanField(null=False)
    precio= models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "XBOX"
        verbose_name_plural = "XBOX"

    @property
    def precio_con_simbolo(self):
        return f'€{self.precio}'

    def __str__(self):
        return f"{self.nombre}"

class Otras_consolas(models.Model):
    PLATAFORMA_CHOICES = (
        ('PS4', 'PS4'),
        ('XBOX ONE', 'XBOX ONE'),
        ('Nintendo Switch', 'Nintendo Switch'),
        ('PC', 'PC'),
    )
    nombre= models.CharField(max_length=60)
    plataforma= models.CharField(max_length=30, choices=PLATAFORMA_CHOICES)
    genero= models.CharField(max_length=15)
    online= models.BooleanField()
    precio= models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Otras Consolas"
        verbose_name_plural = "Otras Consolas"

    @property
    def precio_con_simbolo(self):
        return f'€{self.precio}'
    
    def __str__(self):
        return f"{self.nombre}"

class Socios(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    edad= models.IntegerField()

    class Meta:
        verbose_name = "Socios"
        verbose_name_plural = "Socios"
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class XBOXForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=60, required=True)
    genero= forms.CharField(label="Género", max_length=15, required=True)
    online= forms.BooleanField(label="Tiene online?", required=True)
    precio= forms.DecimalField(label="Precio", decimal_places=2, required=True)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"