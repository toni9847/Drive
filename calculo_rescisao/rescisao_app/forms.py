from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'other_field_name', 'another_field_name']
