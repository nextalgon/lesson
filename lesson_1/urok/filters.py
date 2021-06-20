import django_filters
from .models import Pupil


class PupilFilter(django_filters.FilterSet):

    class Meta:
        model = Pupil
        fields = {
            'ism': ['icontains']
        }
