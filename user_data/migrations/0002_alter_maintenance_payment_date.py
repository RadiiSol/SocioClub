# Generated by Django 3.2.7 on 2022-07-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='payment_date',
            field=models.DateField(null=True),
        ),
    ]
