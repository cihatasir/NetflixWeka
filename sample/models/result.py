from django.db import models

class ResultModel(models.Model):
    film_result= models.CharField(max_length=150)

    class Meta:
        db_table = 'result'

    def __str__(self):
        return self.film_result

