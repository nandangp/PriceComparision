# Generated by Django 4.2.2 on 2023-09-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prizes",
            fields=[
                ("p_no", models.AutoField(primary_key=True, serialize=False)),
                ("p_name", models.CharField(max_length=50)),
                ("p_img", models.URLField()),
                ("f_prize", models.IntegerField()),
                ("a_prize", models.IntegerField()),
                ("r_prize", models.IntegerField()),
            ],
        ),
    ]