# Generated by Django 3.1.4 on 2022-03-22 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0017_auto_20220309_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='name_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='music',
            name='share',
            field=models.CharField(default='NqyngIAkOtTSSwbbUjbFuxndPQWugvYfRkFXGRxwOBPhGGoTQA', max_length=50),
        ),
    ]
