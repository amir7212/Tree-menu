# Generated by Django 5.0.4 on 2024-04-12 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu_tag", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="menu_tag.menu",
            ),
        ),
    ]
