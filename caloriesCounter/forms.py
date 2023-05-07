from django.forms import ModelForm
from .models import *


class CaloriesCounterForm(ModelForm):
    class Meta:
        model = CaloriesCounter
        fields = '__all__'
