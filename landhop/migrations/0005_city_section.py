# Generated by Django 4.1.4 on 2022-12-28 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("landhop", "0004_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="city",
            name="section",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="section",
                to="landhop.section",
            ),
        ),
    ]
