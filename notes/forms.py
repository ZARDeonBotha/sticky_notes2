from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Represents a form for creating or editing Note instances.

    This form is built using Django's ``forms.ModelForm`` class.
    It is specifically designed to work with the ``Note`` model, allowing
    users to input or edit the ``title`` and ``content`` fields of a
    ``Note`` instance.

    :ivar Meta.model: The model class to be used for creating the form.
    :type Meta.model: type
    :ivar Meta.fields: The fields of the model that will be
    included in the form.
    :type Meta.fields: list[str]
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
