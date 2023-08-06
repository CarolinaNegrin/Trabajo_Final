from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    mensaje = forms.CharField(label='mensaje', widget=forms.Textarea)