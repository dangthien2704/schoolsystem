# Generated by Django 3.1.1 on 2020-10-22 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0019_auto_20201022_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='question',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='assignments.question'),
            preserve_default=False,
        ),
    ]
