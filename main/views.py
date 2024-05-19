from django.shortcuts import render

from main.models import Article


# Create your views here.
def index(request):
    # students_list = Student.objects.all()
    context = {}
    return render(request, 'main/index.html')


# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'main/index.html')
