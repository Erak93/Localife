# Generated by Django 4.2.2 on 2023-06-30 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0007_remove_userprofile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="region",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_app.region",
            ),
        ),
    ]