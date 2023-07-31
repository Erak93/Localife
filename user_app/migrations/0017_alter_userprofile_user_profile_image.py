# Generated by Django 4.2.2 on 2023-07-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0016_alter_userprofile_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="user_profile_image",
            field=models.ImageField(
                blank=True,
                default="user_app/snow.jpg",
                null=True,
                upload_to="user_app/profile_pics",
            ),
        ),
    ]
