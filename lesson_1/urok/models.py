from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Classroom(models.Model):
    room = models.CharField(verbose_name='sinfi', max_length=3)

    class Meta:
        verbose_name = 'sinf'
        verbose_name_plural = 'sinflar'

    def __str__(self):
        return self.room


class Pupil(models.Model):
    ism = models.CharField(max_length=50, verbose_name='ism', null=True)
    surname = models.CharField(max_length=50, verbose_name="familya", null=True)
    age = models.CharField(verbose_name="yosh", max_length=30)
    gradue = models.ForeignKey(Classroom, verbose_name='sinfi', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email', null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "o\'quvchi"
        verbose_name_plural = "o\'quvchilar"
