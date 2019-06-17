# Generated by Django 2.2.1 on 2019-06-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplfreak', '0004_auto_20190617_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player_of_the_match',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='toss_winner',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
