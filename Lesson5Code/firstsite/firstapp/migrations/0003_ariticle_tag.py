# Generated by Django 2.1 on 2018-08-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_ariticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='ariticle',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]
