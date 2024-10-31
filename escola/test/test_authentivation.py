from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse

class AuthenticationUserTestCAse(APITestCase):
    def  setUp(self):
        self.usuario = User.objects.create_superuser(username= 'admin', password= 'admin')
        self.url = reverse('Estudantes-list')

    def test_autenticacao_user_com_credenciais_corretas(self):
        '''Teste que verifica se o login está ocorrendo corretamente'''

        usuario = authenticate(username= 'Admin', password= 'Admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticação_user_com_credenciais_corretas(self):
        '''Teste que verifica se o login do usuario esta errado'''
        usuario = authenticate(username= 'Admn', password= 'admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticação_user_com_credenciais_corretas(self):
        '''Teste que verifica se o login do usuario esta errado'''
        usuario = authenticate(username= 'Admin', password= 'admn')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

