# Generated by Django 2.0.2 on 2018-02-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=150)),
                ('subject_Descreption', models.CharField(max_length=200)),
            ],
        ),
    ]
