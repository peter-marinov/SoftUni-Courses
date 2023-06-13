import uuid

from django import forms
from django.core.exceptions import ValidationError

from forms_part_2_demos.web.model_validators import validate_max_todos_per_person
from forms_part_2_demos.web.models import Todo, Person
from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(validate_text,
                    ),
        error_messages={
            'required': 'Todo text must be set!'
        }
    )
    is_done = forms.BooleanField(
        required=False
    )

    priority = forms.IntegerField(
        validators=(
            # validate_priority,
            # build in validators
            # MinValueValidator(1),
            # MaxValueValidator(10),
            ValueInRangeValidator(1, 10),
        )
    )

    def clean_text(self):
        pass

    def clean_priority(self):
        # raise ValidationError('Error!!!!')
        pass

    def clean_is_done(self):
        pass


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self, *args, **kwargs):
        return super().clean()

    def clean_text(self):
        '''
        Used for:
        1. Transform data into desired format/form
        2. Validation
        :return:
        '''
        return self.cleaned_data['text'].lower()

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']

        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            self.cleaned_data['assignee'] = Person.objects.get(name='Unassigned')
            assignee = self.clean_assignee()

        return assignee

    # def clean_assignee(self):
    #     assignee = self.cleaned_data['assignee']
    #     validate_max_todos_per_person(assignee)
    #     return assignee

    def clean(self):
        pass


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name =str(uuid.uuid4())
        return profile_image

    # def clean(self):
    #     super().clean()
    #      # all values are in the cleaned_data
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']