from django.forms import ModelForm
from .models import Author, Quote


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'bio')

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ('text', 'author')
