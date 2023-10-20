from django.contrib.auth import authenticate, login, logout
from django.views import View
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import *

# Create your views here.


class ArticlesView(View):
    def get(self, request: Request) -> Response:
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class LoginAPI(View):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({"message": "Autentificare reușită."}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Autentificare eșuată. Verificați numele de utilizator și parola."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Deautentificare reușită."}, status=status.HTTP_200_OK)
