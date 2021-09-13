from django.urls import path, include
from sample.views import test_form, anasayfa, result_views, restart, delete_films
from django.urls import path, include


urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('form/', test_form, name="form"),
    path('result/', result_views, name="result"),
    path('restart/', restart, name="restart"),
    path('delete/', delete_films, name="delete"),
]
