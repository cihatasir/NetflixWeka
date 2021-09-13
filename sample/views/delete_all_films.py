from sample.models import AllFilms
from django.shortcuts import redirect


def delete_films(request):
    AllFilms.objects.all().delete()
    return redirect('anasayfa')
