from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers

from escola.views import AlunosViewSet
from escola.views import CursosViewSet
from escola.views import MatriculaViewSet
from escola.views import MatriculasAluno
from escola.views import AlunosMatriculados

router = routers.DefaultRouter()

router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', MatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', AlunosMatriculados.as_view())
]
