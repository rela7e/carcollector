from django.forms import ModelForm
from .models import Accolade

class AccoladeForm(ModelForm):
  class Meta:
    model = Accolade
    fields = ['name', 'description']