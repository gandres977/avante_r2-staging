# Generated by Django 4.2.9 on 2024-06-17 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0009_logisticsstate_haulentry_totes_in_staging_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tote',
            name='staged',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='staged_queue', to='avantecore.logisticsstate'),
        ),
    ]
