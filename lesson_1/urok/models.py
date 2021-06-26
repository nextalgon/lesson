from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Classroom(models.Model):
    room = models.CharField(verbose_name='sinfi', max_length=3)
    fan = models.ManyToManyField('Lesson', verbose_name='fan')


    class Meta:
        verbose_name = 'sinf'

    def __str__(self):
        return self.room


class Pupil(models.Model):
    ism = models.CharField(max_length=50, verbose_name='ism', null=True)
    surname = models.CharField(max_length=50, verbose_name="familya", null=True)
    age = models.DateField(verbose_name="yosh")
    gradue = models.ForeignKey(Classroom, verbose_name='sinfi', on_delete=models.CASCADE, null=True)
    email = models.EmailField(verbose_name='email', null=True)
    time = models.DateField(verbose_name='vaxt', null=True, auto_now_add=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "o\'quvchi"
        verbose_name_plural = "o\'quvchilar"


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='fan nomi')
    sinflar = models.ManyToManyField(Pupil, through='Baho')

    def __str__(self):
        return self.name


class Baho(models.Model):
    name = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE,)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    baho = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.baho

    class Meta:
        unique_together = [['name', 'lesson']]
