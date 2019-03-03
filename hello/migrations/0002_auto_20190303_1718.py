# Generated by Django 2.1.7 on 2019-03-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='invEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=21)),
                ('employee', models.IntegerField(default=0)),
                ('beginv', models.IntegerField(default=0)),
                ('endinv', models.IntegerField(default=0)),
                ('actualinv', models.IntegerField(default=0)),
                ('delivery', models.IntegerField(default=0)),
                ('sales', models.IntegerField(default=0)),
                ('salesamount', models.IntegerField(default=0)),
                ('shortage', models.IntegerField(default=0)),
                ('shortageamount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='Date Added')),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]