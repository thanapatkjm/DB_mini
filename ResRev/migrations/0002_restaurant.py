# Generated by Django 2.1.1 on 2019-04-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResRev', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('category', models.TextField()),
                ('rating', models.FloatField(default=0)),
                ('g_rating', models.FloatField(default=0)),
            ],
        ),
    ]