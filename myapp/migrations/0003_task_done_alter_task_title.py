# Generated by Django 4.2.3 on 2023-07-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="done",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
