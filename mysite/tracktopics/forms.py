from django import forms

class AddFieldsForm(forms.Form):
    topic = forms.CharField(label='topic', max_length=100)
    word = forms.CharField(label='word', max_length=100)
    user = forms.CharField(label='user', max_length=100)