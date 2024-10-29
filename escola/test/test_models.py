from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'test do mudelo de estudante',
            email = 'test@gmail.com',
            cpf = '48521353049',
            data_nascimento = '2000-12-02',
            celular = '84 99999-9999')

    def test_verifica_atributos_de_estudante(self):
        '''Testa os atributos de um aluno quado ele criado na base de dados'''
        self.assertEqual(self.estudante.nome, 'test do mudelo de estudante')
        self.assertEqual(self.estudante.email, 'test@gmail.com')
        self.assertEqual(self.estudante.cpf, '48521353049')
        self.assertEqual(self.estudante.data_nascimento, '2000-12-02')
        self.assertEqual(self.estudante.celular, '84 99999-9999')

class ModelCursotestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CWD1',
            descricao = 'curso web design',
            nivel = 'Avançado',
        )

    def test_verifica_atributos_de_estudante(self):
        self.assertEqual(self.curso.codigo, 'CWD1')
        self.assertEqual(self.curso.descricao, 'curso web design' )
        self.assertEqual(self.curso.nivel, 'Avançado' )


    class ModelmatriculasTestcase(TestCase):
        def setUp(self):
            self.estudante = Estudante.objects.create(
                nome = 'test do mudelo de estudante',
                email = 'test@gmail.com',
                cpf = '48521353049',
                data_nascimento = '2000-12-02',
                celular = '84 99999-9999')
        
            self.curso = Curso.objects.create(
                codigo = 'CWD1',
                descricao = 'curso web design',
                nivel = 'Avançado',
            )

            self.matricula = Matricula.objects.create(
                periodo = "Noturno"
            )

        def test_verifica_atributos_de_estudante(self):
            self.assertEqual(self.estudante.nome, 'test do mudelo de estudante')
            self.assertEqual(self.estudante.email, 'test@gmail.com')
            self.assertEqual(self.estudante.cpf, '48521353049')
            self.assertEqual(self.estudante.data_nascimento, '2000-12-02')
            self.assertEqual(self.estudante.celular, '84 99999-9999')

            self.assertEqual(self.curso.codigo, 'CWD1')
            self.assertEqual(self.curso.descricao, 'curso web design' )
            self.assertEqual(self.curso.nivel, 'Avançado' )

            self.assertEqual(self.matricula.periodo, 'Norturno')