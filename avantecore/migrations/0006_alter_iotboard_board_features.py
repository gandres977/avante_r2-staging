# Generated by Django 4.2.9 on 2024-06-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0005_alter_iotboard_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iotboard',
            name='board_features',
            field=models.ManyToManyField(to='avantecore.iotboardfeatures'),
        ),
    ]
