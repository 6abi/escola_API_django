from rest_framework import  serializers
from escola.models import  Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
    """ Dados dos alunos que serão disponibilizados na API
    """""
    model = Aluno
    fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    """ Dados dos cursos que serão disponibilizados na API
    """""
    model = Curso
    fields = '__all__'