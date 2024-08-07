# Generated by Django 5.0.7 on 2024-07-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50)),
                ('date_eaten', models.DateField()),
                ('comment', models.CharField(max_length=280)),
                ('taste_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('aesthetic_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('aroma_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
