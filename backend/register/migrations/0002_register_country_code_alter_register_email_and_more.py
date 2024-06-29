# Generated by Django 5.0.6 on 2024-06-28 23:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='country_code',
            field=models.CharField(default=55, max_length=4, validators=[django.core.validators.RegexValidator('^\\+\\d{1,3}$', 'O código do país deve estar no formato +[código]')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastname',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Apenas letras são permitidas')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Apenas letras são permitidas')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='whatsapp',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{10,15}$', 'O número do WhatsApp deve conter entre 10 a 15 dígitos')]),
        ),
    ]