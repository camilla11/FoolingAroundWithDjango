from django import forms

class AddTopicForm(forms.Form):
    topic = forms.CharField(label='Topic Name', max_length=100)
    
class AddWordForm(forms.Form):
    word = forms.CharField(label='Add new word', max_length=100)
    
class AddUserForm(forms.Form):
    user = forms.CharField(label='Add new user', max_length=100)