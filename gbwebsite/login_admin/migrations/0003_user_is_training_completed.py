# Generated by Django 3.2.6 on 2021-08-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_admin', '0002_remove_user_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_training_completed',
            field=models.BooleanField(default=False),
        ),
    ]
