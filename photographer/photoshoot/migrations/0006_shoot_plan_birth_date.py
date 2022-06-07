# Generated by Django 4.0.3 on 2022-05-02 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photoshoot', '0005_remove_shoot_plan_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoot_plan',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]