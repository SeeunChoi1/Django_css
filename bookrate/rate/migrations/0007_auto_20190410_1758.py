# Generated by Django 2.2 on 2019-04-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0006_auto_20190410_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='star_rate',
            field=models.IntegerField(choices=[(5, '⭐️⭐️⭐️⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (3, '⭐️⭐️⭐️'), (2, '⭐️⭐️'), (1, '⭐️')], default=1),
        ),
    ]