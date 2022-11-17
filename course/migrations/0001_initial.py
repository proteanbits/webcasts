# Generated by Django 4.1.3 on 2022-11-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_desc', models.CharField(blank=True, max_length=250, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]