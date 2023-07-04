# Generated by Django 4.2.2 on 2023-07-04 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("region_name", models.CharField(max_length=255)),
                ("region_desc", models.TextField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name="userprofile",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="userprofile_set",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                related_name="userprofile_set",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="location",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user_profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="user_app/profile_pics"
            ),
        ),
    ]
