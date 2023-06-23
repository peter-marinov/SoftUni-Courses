from django import forms

from june_27_2021.notes_app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BaseNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class AddNoteForm(BaseNoteForm):
    pass


class EditNoteForm(BaseNoteForm):
    pass


class DeleteNoteForm(BaseNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            print(field)
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
