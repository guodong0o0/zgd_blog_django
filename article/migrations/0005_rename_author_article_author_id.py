# Generated by Django 4.2.4 on 2023-08-06 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_rename_author_id_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='author_id',
        ),
    ]
