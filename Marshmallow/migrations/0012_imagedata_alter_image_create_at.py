# Generated by Django 4.0.2 on 2023-05-25 13:16

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Marshmallow', '0011_remove_image_image_image_create_at_image_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='imageData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data', models.BinaryField()),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
