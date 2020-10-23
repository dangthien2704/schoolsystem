# Generated by Django 3.1.1 on 2020-10-21 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0013_delete_studentanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignment')),
                ('choice_of_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]