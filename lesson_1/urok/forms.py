from django.forms import ModelForm, NumberInput, TextInput, EmailInput, DateInput
from .models import Pupil, Classroom, Baho


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['room', 'fan']
        widgets = {
            "room": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'sinfni kiriting'}),
        }


class PupilForm(ModelForm, NumberInput, TextInput, EmailInput):
    class Meta:
        model = Pupil
        fields = ['ism', 'surname', 'age', 'email', 'gradue']
        widgets = {
            "ism": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ismini kiriting'}),

            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'familyasini kiriting'}),

            "age": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'yoshini kiriting'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'emailni kiriting'
            })
        }


class BahoForm(ModelForm):
    class Meta:
        model = Baho
        fields = ['name', 'lesson', 'baho']
