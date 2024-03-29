# Generated by Django 4.2.3 on 2023-07-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_smartstore_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('otp', models.IntegerField()),
                ('validity', models.DateTimeField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
