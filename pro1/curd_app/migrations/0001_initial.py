# Generated by Django 5.0.3 on 2024-03-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('booking_date_time', models.DateField()),
                ('aadhar_no', models.IntegerField()),
                ('type', models.CharField(choices=[('MEN', 'men'), ('WOMEN', 'women'), ('OTHER', 'other')], max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
