# Generated by Django 3.1.4 on 2022-03-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20220308_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='share',
            field=models.CharField(default='LpiSPcsxqohLyZzcaGqJibdEqCXkMQFIpaIdYDnRbntRxKQrQQ', max_length=50),
        ),
    ]
