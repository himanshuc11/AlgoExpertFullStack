# Generated by Django 4.0.1 on 2022-01-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_alter_problemlist_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemlist',
            name='start_code',
            field=models.TextField(default='TODO'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problemlist',
            name='type',
            field=models.CharField(default='TODO', max_length=128),
            preserve_default=False,
        ),
    ]
