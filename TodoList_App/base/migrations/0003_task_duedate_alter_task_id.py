# Generated by Django 4.2 on 2023-05-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210322_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]