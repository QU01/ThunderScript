from django import forms

class cmsmap(forms.Form):

    website = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'URL'}), max_length=50, label='',required=True)

class zero(forms.Form):

    website = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'EMAIL'}), max_length=50, label='',required=True)

class mack(forms.Form):

    IP = forms.CharField(label='IP', max_length=100)
