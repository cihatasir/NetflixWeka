from django.shortcuts import render
from sample.models import AllFilms

def restart(request):
    all_films = AllFilms.objects.all()

    context = {
        'all_films': all_films,
    }

    return render(request, 'restart.html', context)

