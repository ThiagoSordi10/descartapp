# Generated by Django 4.0 on 2022-11-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discard', '0003_order_discarder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('a', 'Accepted'), ('r', 'Refused'), ('p', 'Pending'), ('f', 'Finished')], default='p', max_length=1),
        ),
    ]