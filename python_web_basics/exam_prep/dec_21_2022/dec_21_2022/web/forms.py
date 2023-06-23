from django import forms

from dec_21_2022.web.models import Profile, Plant


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class EditProfileForm(BaseProfileForm):
    pass


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'

