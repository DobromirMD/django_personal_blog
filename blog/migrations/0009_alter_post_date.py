# Generated by Django 4.2.7 on 2023-12-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
