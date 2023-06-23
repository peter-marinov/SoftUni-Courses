from django import forms

from aug_11_2021.online_library.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(BaseProfileForm):
    pass


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'URL'
                }
            ),
        }


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()

    def __disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AddBookForm(BaseBookForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crtime...'
                }
            ),
        }


class EditBookForm(BaseBookForm):
    pass
