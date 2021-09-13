from django import forms

COUNTRY = [
    ('United States', 'United States'),
    ('United Kingdom', 'United Kingdom'),
    ('Canada', 'Canada'),
    ('Turkey', 'Turkey'),
    ('France', 'France'),
    ('Germany', 'Germany'),
    ('India', 'India'),
]

RATING = [
    ('G', 'G'),
    ('NR', 'NR'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
    ('TV-14', 'TV-14'),
    ('TV-G', 'TV-G'),
    ('TV-MA', 'TV-MA'),
    ('TV-PG', 'TV-PG'),
    ('TV-Y', 'TV-Y'),
    ('TV-Y7', 'TV-Y7'),
]

GENRE = [
    ('Action & Adventure', 'Action & Adventure'),
    ('Dramas', 'Dramas'),
    ('Horror Movies', 'Horror Movies'),
    ('Documentaries', 'Documentaries'),
    ('Comedies', 'Comedies'),
    ('Children & Family Movies', 'Children & Family Movies'),
    ('Stand-Up Comedy', 'Stand-Up Comedy'),
]


class ChooseForm(forms.Form):

    _country = forms.CharField(label='Country  ',
                                     widget=forms.Select(choices=COUNTRY))

    _rating = forms.CharField(label='Rating  ',
                                     widget=forms.Select(choices=RATING))

    _genre = forms.CharField(label='Genre  ',
                                     widget=forms.Select(choices=GENRE))


    _duration = forms.CharField(max_length=100, label='Duration  ')


