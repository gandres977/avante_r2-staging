# Generated by Django 4.2.9 on 2024-06-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0007_alter_iotboard_image_alter_smartedgesensor_btle_mac_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LedgerEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('event_reference', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='spirit',
            field=models.CharField(default='SPIRIT-NA', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerdispatchlocation',
            name='spirit',
            field=models.CharField(default='SPIRIT-NA', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='spirit',
            field=models.CharField(default='SPIRIT-NA', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providerdispatchlocation',
            name='spirit',
            field=models.CharField(default='SPIRIT-NA', max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EnvironmentEntry',
        ),
    ]