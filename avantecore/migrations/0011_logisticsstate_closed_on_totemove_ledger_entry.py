# Generated by Django 4.2.9 on 2024-06-17 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0010_alter_tote_staged'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticsstate',
            name='closed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='totemove',
            name='ledger_entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='avantecore.ledgerentry'),
        ),
    ]
