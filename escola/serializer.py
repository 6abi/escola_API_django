from rest_framework import  serializers
from escola.models import  Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    """ Dados dos alunos que serão disponibilizados na API
    """""
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento'] #traz as info desse campos da base
class CursoSerializer(serializers.ModelSerializer):
    """ Dados dos cursos que serão disponibilizados na API
    """""
    class Meta:
        model = Curso
        fields = '__all__' #traz todas as info da base

class MatriculaSerializer(serializers.ModelSerializer):
    """Dados das matriculas"""

    class Meta:
        model = Matricula
        exclude = [] #traz todas as info da base