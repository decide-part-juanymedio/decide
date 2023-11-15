from django import forms
from voting.models import *

class CensusReuseForm(forms.Form):
    oldVoting = forms.ModelChoiceField(label='Votacion de la que se va a reutilizar censo', queryset=Voting.objects.all(), required=True)
    newVoting = forms.ModelChoiceField(label='Votacion a la que se va a copiar censo', queryset=Voting.objects.all(), required=True)