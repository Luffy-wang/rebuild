# Generated by Django 2.0.3 on 2018-03-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0002_auto_20180313_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.CharField(db_index=True, max_length=32, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.CharField(max_length=30)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=30)),
                ('code', models.TextField()),
                ('result', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('problem', models.ForeignKey(on_delete=True, to='problem.Problem')),
            ],
            options={
                'db_table': 'Submission',
            },
        ),
    ]