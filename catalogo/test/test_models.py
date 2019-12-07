from django.test import TestCase
from muebleria.models import Formulario


class FormularioModelTest(TestCase):
    @classmethod
    def setUpData(cls):
        Formulario.objects.create(id = "6",nombre="jaime",rut="20379558-2",num_cont="+56964350008", email="jaime123@gmail.com",mensaje='se guardo correctamente la prueba')
    def test_id_label(self):
        Fo= Formulario.objects.get(id = '6')
        field_label = Fo._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')