# Generated by Django 4.2.6 on 2023-10-20 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='id',
        ),
        migrations.AddField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
