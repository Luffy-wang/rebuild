# Generated by Django 2.0.3 on 2018-04-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0011_auto_20180403_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classhomework',
            name='problem_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
    ]
