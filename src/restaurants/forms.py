from django import forms


class ScoreCreateForm(forms.Form):
     Call_number = forms.CharField()
     Score_title= forms.CharField(required=False)
     author = forms.CharField(required=False)
     place_of_publication = forms.CharField(required=False)
     date_of_publication = forms.CharField(required=False)
     publisher = forms.CharField(required=False)