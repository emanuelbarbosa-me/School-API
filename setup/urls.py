from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação da API",
        default_version='v1',
        description="Descrição da API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@exemplo.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
    path('api/v2/estudantes/', EstudanteViewSet.as_view({'get': 'list_v2', 'post': 'create_v2'}), name='estudante-list-v2'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
