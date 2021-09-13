from django.shortcuts import render, redirect
from sample.forms import ChooseForm
from main import *
import weka.core.jvm as jvm
from weka.classifiers import PredictionOutput
import os
from sample.models import ResultModel, AllFilms


def test_form(request):
    form = ChooseForm()

    if request.method == 'POST':
        form = ChooseForm(request.POST)

        if form.is_valid():

            country = form['_country'].value()
            rating = form['_rating'].value()
            genre = form['_genre'].value()
            duration = form['_duration'].value()

            if jvm.started:
                return redirect('restart')

            else:
                jvm.start()
                cloneData(country, rating, duration, genre)
                filmName = loadDataSet()
                save_result_model = ResultModel(film_result=filmName)
                save_result_model.save()

                save_all_films = AllFilms(all_films_result=filmName)
                save_all_films.save()

            return redirect('result')

    context = {
        'form': form,
    }

    return render(request, "form.html", context)




