from django import forms
import django_filters
from Music.models import Music


class MusicFilter(django_filters.FilterSet):
    class Meta:
        model = Music
        fields = {
            'music_name': ['icontains', ],
            'music_brand': ['exact', ],
            'music_quantity': ['gt', 'range'],
            'music_producer': ['startswith'],
        }

