# Generated by Django 4.0.3 on 2023-05-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marshmallow', '0005_board_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='board',
            name='image',
        ),
    ]
