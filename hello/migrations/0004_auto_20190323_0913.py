# Generated by Django 2.1.7 on 2019-03-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20190323_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventry',
            name='actualinv',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='inventry',
            name='shortage',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='inventry',
            name='shortageamount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
