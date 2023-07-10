from django.shortcuts import render
from mainApp.models import Blanks


# Create your views here.
def main_show_page(request):
    persons = Blanks.objects.all()
    context = {'persons': persons}
    return render(request, 'main.html', context=context)


def more_info_show_page(request, param):
    men = Blanks.objects.get(pk=param)
    context = {'men': men}
    return render(request, 'moreInfo.html', context=context)


def create_blank_show_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        country = request.POST.get('country')
        bio = request.POST.get('bio')

        Blanks.objects.create(email=email,
                              password=password,
                              name=name,
                              surname=surname,
                              age=age,
                              country=country,
                              bio=bio)

    return render(request, 'create.html')

