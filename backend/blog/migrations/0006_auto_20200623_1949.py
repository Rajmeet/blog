# Generated by Django 3.0.7 on 2020-06-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200622_2025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsletterUser',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
