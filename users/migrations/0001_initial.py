# Generated by Django 5.1.3 on 2024-11-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_name", models.CharField(max_length=50)),
                ("user_email", models.EmailField(max_length=50)),
                ("user_password", models.CharField(max_length=50)),
                ("gender", models.CharField(choices=[("M", "Male"), ("F", "Female")], max_length=1)),
                ("phone_number", models.CharField(max_length=50)),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
                ("self_introduced", models.TextField(blank=True, null=True)),
                ("portfolio", models.BinaryField(null=True)),
                ("birthday", models.DateField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]