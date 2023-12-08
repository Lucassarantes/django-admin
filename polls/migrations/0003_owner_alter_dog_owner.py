# Generated by Django 5.0 on 2023-12-08 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_dog_owner_alter_dog_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.owner'),
        ),
    ]
