# Generated by Django 4.2.6 on 2023-10-24 09:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Notes', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
