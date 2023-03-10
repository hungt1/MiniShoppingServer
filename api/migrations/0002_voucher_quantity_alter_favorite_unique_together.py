# Generated by Django 4.0.6 on 2023-01-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'product')},
        ),
    ]
