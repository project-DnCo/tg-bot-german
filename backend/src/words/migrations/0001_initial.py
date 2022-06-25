# Generated by Django 4.0.5 on 2022-06-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('der', 'Der'), ('die', 'Die'), ('das', 'Das')], max_length=3)),
            ],
        ),
    ]