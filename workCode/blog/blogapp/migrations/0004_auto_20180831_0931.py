# Generated by Django 2.1 on 2018-08-31 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20180831_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='mod_date',
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]