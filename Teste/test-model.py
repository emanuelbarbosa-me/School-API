import pytest
from escola.models import Curso, Estudante, Matricula

@pytest.mark.django_db
def test_curso_criacao():
    curso = Curso.objects.create(codigo='C001', descricao='Curso de Exemplo', nivel='B')
    assert curso.codigo == 'C001'
    assert curso.descricao == 'Curso de Exemplo'
    assert curso.nivel == 'B'

@pytest.mark.django_db
def test_matricula_criacao():
    estudante = Estudante.objects.create(
        nome='João Silva',
        email='joao@example.com',
        cpf='12345678901',
        data_nascimento='2000-01-01',
        celular='1234567890'
    )
    curso = Curso.objects.create(codigo='C001', descricao='Curso de Exemplo', nivel='B')
    matricula = Matricula.objects.create(estudante=estudante, curso=curso, periodo='M')

    assert matricula.estudante == estudante
    assert matricula.curso == curso
    assert matricula.periodo == 'M'

@pytest.mark.django_db
def test_estudante_criacao():
    estudante = Estudante.objects.create(
        nome='João Silva',
        email='joao@example.com',
        cpf='12345678901',
        data_nascimento='2000-01-01',
        celular='1234567890'
    )
    assert estudante.nome == 'João Silva'
    assert estudante.cpf == '12345678901'

