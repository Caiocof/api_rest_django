from _ast import Is

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno
from escola.models import Curso
from escola.models import Matricula
from escola.serializer import AlunoSerializer
from escola.serializer import CursoSerializer
from escola.serializer import MatriculaSerializer
from escola.serializer import MatriculasAlunoSerializer
from escola.serializer import AlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasAluno(generics.ListAPIView):
    """Lista todos as matriculas de um aluno(a)"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = MatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AlunosMatriculados(generics.ListAPIView):
    """Lista todos os alunos(as) matriculado em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = AlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
