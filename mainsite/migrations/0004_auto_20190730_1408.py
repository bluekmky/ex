# Generated by Django 2.2.1 on 2019-07-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20190728_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentid',
            field=models.IntegerField(null=True),
        ),
    ]