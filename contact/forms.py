from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome')
    telefone = forms.CharField(label='Telefone', required=False) 
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(widget=forms.Textarea)