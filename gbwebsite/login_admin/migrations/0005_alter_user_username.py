# Generated by Django 3.2.6 on 2021-09-02 13:16

from django.db import migrations, models
import login_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('login_admin', '0004_user_is_assessment_passed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[login_admin.models.name_validator()], verbose_name='username'),
        ),
    ]
