# Generated by Django 4.2.16 on 2024-12-13 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_now', '0005_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['created_on']},
        ),
    ]