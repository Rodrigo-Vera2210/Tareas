import pytest
from django.test import TestCase, Client
from apps.tarea.models import *
from ddf import G, N

"""
@pytest.fixture
def tarea_creation():
    return N(Tarea)

@pytest.mark.django_db
def test_tarea_creation(tarea_creation):
    print(tarea_creation.nombre)
    tarea_creation.save()
    assert tarea_creation.estado == False

@pytest.mark.django_db
def test_tarea_creation_fail():
    with pytest.raises(Exception):
        Tarea.objects.create(
            nombre = 'casa',
            estado = 'sada'
        )
"""

class TareaTestCase(TestCase):

    def setUp(self):
        self.tarea = Tarea.objects.create(
            nombre = 'Pedro',
            estado = False
        )
        self.client = Client()

    def test_tarea_creation(self):
        self.assertEquals(self.tarea.estado, False)
        assert self.tarea.nombre == 'Pedro'

    def test_list(self):
        response = self.client.get(
            '/tarea/'
        )
        print(response.status_code)
        print(response.content)

    def test_crear(self):
        response = self.client.post(
            '/tarea/crear/',
            {
                'nombre': 'admin',
                'estado': False,
            }
        )
        print(response.status_code)
        print(response.content)

    def test_editar(self):
        response = self.client.put(
            '/tarea/update/5',
            {
                'nombre': 'adsada',
                'estado': True
            }
        )
        print(response.status_code)
        print(response.content)

    def test_eliminar(self):
        response = self.client.delete(
            '/tarea/delete/5'
        )
        print(response.status_code)
        print(response.content)





