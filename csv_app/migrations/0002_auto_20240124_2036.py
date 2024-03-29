# Generated by Django 3.2.22 on 2024-01-24 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csv_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialdata',
            name='chge_revenues',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='pre_tax_op_income',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_app.stock'),
        ),
    ]
