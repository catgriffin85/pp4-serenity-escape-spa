# Generated by Django 4.2.16 on 2024-12-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_now', '0006_alter_review_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
