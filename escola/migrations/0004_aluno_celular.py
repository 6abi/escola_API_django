# Generated by Django 3.1.3 on 2021-07-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_auto_20210708_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
    ]
