# Generated by Django 2.1.8 on 2019-11-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('age', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=10, null=True)),
                ('picture', models.ImageField(default='Muser/image/11.jpeg', upload_to='Muser/images')),
            ],
        ),
    ]