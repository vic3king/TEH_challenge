# Generated by Django 2.2.5 on 2019-09-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('job_poaition', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]