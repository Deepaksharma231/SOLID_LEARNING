# Generated by Django 3.2.3 on 2021-06-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('Name', models.CharField(max_length=40)),
                ('Whatshap', models.IntegerField()),
                ('Contact', models.IntegerField()),
                ('State', models.CharField(max_length=40)),
            ],
        ),
    ]