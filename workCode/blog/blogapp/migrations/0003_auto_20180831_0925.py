# Generated by Django 2.1 on 2018-08-31 01:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AddField(
            model_name='article',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改日期'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('life', 'Life'), ('tech', 'Tech')], max_length=5, null=True),
        ),
    ]
