# Generated by Django 3.2.8 on 2022-03-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='feat',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='share',
            field=models.CharField(default='irTMnttlPlmtxYPLapMVXQMDvgUDmyxZJqZWMoWYiAdObHRGGR', max_length=50),
        ),
    ]
