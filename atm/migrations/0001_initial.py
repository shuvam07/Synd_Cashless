# Generated by Django 2.2.1 on 2019-09-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('pin', models.IntegerField(max_length=4)),
                ('otp', models.CharField(max_length=6)),
            ],
        ),
    ]