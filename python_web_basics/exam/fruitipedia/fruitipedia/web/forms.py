from django import forms

from fruitipedia.web.models import ProfileModel, FruitModel


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label = ''

    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image_url', 'age']


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            FruitModel.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = FruitModel
        fields = ()


class CreateFruitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label = ''

    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                },
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                },
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                },
            ),
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class DeleteFruitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    class Meta:
        model = FruitModel
        fields = '__all__'
        exclude = ['nutrition']
