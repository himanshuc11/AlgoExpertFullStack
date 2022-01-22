# Generated by Django 4.0.1 on 2022-01-22 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0008_remove_problemlist_type_problemlist_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemlist',
            name='tier',
            field=models.CharField(choices=[('F', 'FREE'), ('P', 'PAID')], default='P', max_length=16),
        ),
    ]
