from django import forms

from april_19_2022.gamesplay_app.models import ProfileModel, GameModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

