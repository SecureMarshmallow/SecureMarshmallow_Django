# Generated by Django 4.0.2 on 2023-06-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marshmallow', '0019_alter_marshmallow_user_refreshtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
