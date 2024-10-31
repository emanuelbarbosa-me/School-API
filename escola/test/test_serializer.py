from django.test import TestCase
from escola.models import Estudante
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class EstudanteSerializerTest(TestCase):
    def setUp(self):
        self.estudante_info = {
            "id" : '123456',
            "nome" : 'emanuel',
            "email" : 'emg@mail.com',
            "cpf" : '10183726014',
            "data_nascimento" : '2050-12-03',
            "celular" : '84 99999-999',
        }

        self.estudante = Estudante.objects.create(**self.estudante_info)

    def test_serializer_com_dados_validos(self):
        serializer = EstudanteSerializer(instance=self.estudante)
        self.assertEqual(serializer.data, self.estudante_info)


    def test_serializer_com_dados_validos(self):
        dados_invalidos = {
            "nome" : '',
            "email" : 'emgmail.com',
            "cpf" : '10183726014',
            "data_nascimento" : '2050-12-03',
            "celular" : '84 99999-999',
            }

        serializer = EstudanteSerializer(data=dados_invalidos)
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome', serializer.errors)

    def test_criacao_de_estudante(self):
        serializer = EstudanteSerializer(data=self.estudante_info)
        self.assertTrue(serializer.is_valid())
        print(serializer.errors)  # Para depuração
        estudante_criado = serializer.save()
        self.assertEqual(estudante_criado.nome, self.estudante_info['nome'])


    def test_criacao_de_estudante(self):
        serializer = EstudanteSerializer(data=self.estudante_info)
        is_valid = serializer.is_valid()
        print(serializer.errors)  # Isso vai te mostrar os erros
        self.assertTrue(is_valid, msg=str(serializer.errors))
        estudante_criado = serializer.save()
        self.assertEqual(estudante_criado.nome, self.estudante_info['nome'])
