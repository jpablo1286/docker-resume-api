# Generated by Django 2.1.3 on 2018-11-21 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_award_code_expirience_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.TextField(),
        ),
    ]