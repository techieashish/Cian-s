import django_filters
from .models import Candidate

class CandiFilter(django_filters.FilterSet):

    class Meta:
        model = Candidate
        fields = "__all__"

