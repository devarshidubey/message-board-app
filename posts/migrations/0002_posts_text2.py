# Generated by Django 3.1.14 on 2023-01-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='text2',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
