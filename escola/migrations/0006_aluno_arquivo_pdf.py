# Generated by Django 3.1.3 on 2021-07-09 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_aluno_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='arquivo_pdf',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
    ]
