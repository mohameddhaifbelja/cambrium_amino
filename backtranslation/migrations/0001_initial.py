# Generated by Django 3.2.7 on 2021-11-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amino_acid', models.TextField(max_length=1)),
                ('probability', models.FloatField()),
                ('first_choice', models.TextField()),
                ('second_choice', models.TextField()),
            ],
        ),
    ]