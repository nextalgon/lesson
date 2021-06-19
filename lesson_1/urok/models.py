from django.db import models


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
    time = models.DateField(verbose_name='vaxt', null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "o\'quvchi"
        verbose_name_plural = "o\'quvchilar"
