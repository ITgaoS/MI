# Generated by Django 2.1.8 on 2019-11-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Muser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='backstage/images/11.jpeg', upload_to='backstage/images'),
        ),
    ]
