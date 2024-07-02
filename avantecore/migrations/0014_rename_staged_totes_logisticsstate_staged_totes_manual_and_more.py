# Generated by Django 4.2.9 on 2024-06-23 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avantecore', '0013_haulentry_ledger_entry_scaleentry_ledger_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logisticsstate',
            old_name='staged_totes',
            new_name='staged_totes_manual',
        ),
        migrations.AddField(
            model_name='tote',
            name='tips_calculated',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tote',
            name='tips_manual',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scaleentry',
            name='tote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tip', to='avantecore.tote'),
        ),
    ]