from django.views import View
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


class ArticlesView(View):
    def get(self, request: Request) -> Response:
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
