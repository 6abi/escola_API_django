from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import  reverse

class CursosTestCase(APITestCase):

    def SetUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao='Curso teste 1'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso teste 2', nivel='A'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou propositalmente')