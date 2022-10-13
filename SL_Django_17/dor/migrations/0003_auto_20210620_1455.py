# Generated by Django 3.2.3 on 2021-06-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dor', '0002_auto_20210620_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('Contactno', models.IntegerField()),
                ('College', models.CharField(max_length=40)),
                ('InternField', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Issue',
            field=models.CharField(max_length=100),
        ),
    ]