from django.contrib import admin
from django.urls import path, include
from sample.views import test_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sample.urls'))
]
