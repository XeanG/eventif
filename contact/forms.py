from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label='name')
    telefone = forms.CharField(label='phone', required=False) 
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(widget=forms.Textarea)