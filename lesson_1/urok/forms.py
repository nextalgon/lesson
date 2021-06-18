from django.forms import ModelForm, NumberInput, TextInput, EmailInput
from .models import Pupil, Classroom


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['room']
        widgets = {
            "room": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'sinfni kiriting'})}


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

            "age": NumberInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'yoshini kiriting'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'emailni kiriting'
            })
        }
