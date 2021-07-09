from rest_framework.test import APITestCase
from escola.models import  Aluno
from django.urls import  reverse

def AlunoTestCase(APITestCase):

    def SetUp(self):
        self.list_url = reverse('Alunos-list')
        self.aluno_1 = Aluno.objects.create(
            nome= 'Aluno teste', rg = '123456789', cpf = '12345678912', data_nascimento = '06-06-2000', celular = '1145678912'
        )

    def test_falhador(self):
        self.fail('Teste aluno falhou propositalmente')

