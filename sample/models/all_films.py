from django.db import models

class AllFilms(models.Model):
    all_films_result = models.CharField(max_length=300)

    class Meta:
        db_table = 'all'

    def __str__(self):
        return self.all_films_result

