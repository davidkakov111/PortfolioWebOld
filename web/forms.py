from django import forms

#Form for contact.html .
themes = [('Job Opportunity','Job Opportunity'), ('Other','Other'), ('Test','Test')]
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(attrs={'placeholder':'Steve'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'your_real_email@email.com'}))
    themes = forms.ChoiceField(choices=themes, label="Theme")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'placeholder':'Write a message...'}))
