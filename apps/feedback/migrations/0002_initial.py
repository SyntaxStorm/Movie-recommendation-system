# Generated by Django 4.2 on 2023-04-16 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0001_initial'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='films.film'),
        ),
    ]
