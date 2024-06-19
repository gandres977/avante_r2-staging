# Generated by Django 4.2.9 on 2024-06-14 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0006_alter_iotboard_board_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iotboard',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='djangouploads/files/sensor_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='btle_mac',
            field=models.CharField(blank=True, default='', max_length=17),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='eth0_mac',
            field=models.CharField(blank=True, default='', max_length=17),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='eth1_mac',
            field=models.CharField(blank=True, default='', max_length=17),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='djangouploads/filessensor_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='sensor_iot_board',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='avantecore.iotboard'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartedgesensor',
            name='serial_num',
            field=models.CharField(blank=True, default='', max_length=150),
            preserve_default=False,
        ),
    ]
