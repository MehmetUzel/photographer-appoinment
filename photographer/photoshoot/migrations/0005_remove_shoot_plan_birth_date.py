# Generated by Django 4.0.3 on 2022-05-02 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshoot', '0004_alter_shoot_plan_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoot_plan',
            name='birth_date',
        ),
    ]
