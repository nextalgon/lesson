# Generated by Django 3.2.4 on 2021-06-20 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urok', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='fan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urok.lesson', verbose_name='fan'),
        ),
    ]
