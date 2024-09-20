from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            'title': 'Title',
            'text': 'what is on your mind?'
        }

        # def clean_title(self):
        #     title = self.cleaned_data['title']
        #     if len(title) < 5:
        #         raise forms.ValidationError("Title is too short")
        #     return title
