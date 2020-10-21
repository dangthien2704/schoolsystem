# Generated by Django 3.1.1 on 2020-10-20 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0008_auto_20201017_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradedassignment',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gradedassignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='done_assignment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
    ]