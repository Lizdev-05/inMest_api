# Generated by Django 5.0.1 on 2024-03-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_imuser_is_blocked_imuser_permanent_login_fail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imuser',
            name='unique_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
