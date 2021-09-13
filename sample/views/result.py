from django.shortcuts import render
from sample.models import ResultModel


def result_views(request):
    result = ResultModel.objects.all()

    context = {
        'result': result,
    }

    return render(request, 'result.html', context)

