# Generated by Django 2.0.3 on 2018-04-10 14:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.IntegerField()),
                ('class_admin', models.CharField(max_length=30)),
                ('is_activity', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('class_member', models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'myclass',
            },
        ),
    ]
