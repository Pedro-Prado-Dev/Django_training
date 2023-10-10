from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'

    def clean(self):
        nome = self.cleaned_data['name']

        if nome == 'Itajuba':
            raise ValidationError({'nome': 'Não podemos cadastrar a cidade Itajubá no sistema.'})
