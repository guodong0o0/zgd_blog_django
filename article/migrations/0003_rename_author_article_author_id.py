# Generated by Django 4.2.4 on 2023-08-06 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='author_id',
        ),
    ]
