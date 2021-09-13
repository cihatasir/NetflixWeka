from django.shortcuts import render, redirect
from sample.models import ResultModel
import weka.core.jvm as jvm




def anasayfa(request):

    delete_film= ResultModel.objects.all()


    if not delete_film:
        pass

    else:
        delete_film.delete() # delete last value from db


    return render(request, 'anasayfa.html', {})
