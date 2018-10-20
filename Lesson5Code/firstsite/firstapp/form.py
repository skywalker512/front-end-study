from django import forms
from django.core.exceptions import ValidationError


def words_validators(comment):
    if len(comment) < 4:
        raise ValidationError('Not enough words')


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required': 'wow,such words'
            },
        validators=[words_validators]
        )
