# Generated by Django 4.1.1 on 2022-09-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=122)),
                ('mail', models.CharField(max_length=122)),
                ('ph', models.CharField(max_length=12)),
                ('prog', models.CharField(max_length=122)),
                ('goal', models.CharField(max_length=122)),
            ],
        ),
    ]
