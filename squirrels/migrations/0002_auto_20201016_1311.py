# Generated by Django 3.1.2 on 2020-10-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Date',
            field=models.IntegerField(help_text='Date', null=True),
        ),
    ]
