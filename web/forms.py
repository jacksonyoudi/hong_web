from django import forms

class Alogin(forms.Form):
    email = forms.CharField(error_messages={'req'})
    email = forms.CharField(widget=forms.EmailInput(attrs={'css':'add'}))


    def __init__(self):
        self.fields['email'].widget_attrs()