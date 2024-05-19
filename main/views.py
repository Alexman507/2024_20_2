from django.shortcuts import render

from main.models import Article


# Create your views here.
def index(request):
    # model_list = Article.objects.all()
    # context = {}

    return render(request, 'main/templates/main/index.html')
