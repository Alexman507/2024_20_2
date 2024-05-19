from django.shortcuts import render

from main.models import Product, Category, Contact


# Create your views here.
def home(request):
    products_list = Product.objects.all()
    # Product.objects.all().delete()
    #
    #
    context = {
        'object_list': products_list,
        'title': 'Каталог'
    }

    return render(request, 'main/home.html', context)


# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'main/index.html')
