# Generated by Django 4.2.2 on 2023-07-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0006_merge_20230711_0848"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="experience_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/experience_pics"
            ),
        ),
    ]
