# Generated by Django 2.0.3 on 2018-03-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0008_auto_20180331_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]