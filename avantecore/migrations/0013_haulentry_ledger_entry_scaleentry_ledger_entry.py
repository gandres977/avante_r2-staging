# Generated by Django 4.2.9 on 2024-06-17 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0012_logisticsstate_staged_totes_calculated'),
    ]

    operations = [
        migrations.AddField(
            model_name='haulentry',
            name='ledger_entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='avantecore.ledgerentry'),
        ),
        migrations.AddField(
            model_name='scaleentry',
            name='ledger_entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='avantecore.ledgerentry'),
        ),
    ]
