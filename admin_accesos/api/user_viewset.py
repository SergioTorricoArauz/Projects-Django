from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def validate_email_format(email):
    # Expresión regular para validar el formato del correo electrónico
    regex = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'

    if not re.match(regex, email):
        raise ValidationError('El formato del correo electrónico es inválido')


class CreateUserView(APIView):
    @staticmethod
    def post(request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not all([first_name, last_name, username, email, password]):
            return Response({'error': 'Todos los campos son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email_format(email)
        except ValidationError:
            return Response({'error': 'El formato del correo electrónico es inválido'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        user = None

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user
