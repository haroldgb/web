from django.db import models
from django.urls import reverse
import uuid



class Formulario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    rut = models.CharField(max_length=25)
    num_cont = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    mensaje = models.CharField(max_length=25)

    class Meta:
        ordering =['id']


    def get_absolute_url(self):
        return reverse('formulario-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre},{self.rut},{self.num_cont},{self.email},{self.id},{self.mensaje}'