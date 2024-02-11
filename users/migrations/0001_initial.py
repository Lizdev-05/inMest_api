# Generated by Django 5.0.1 on 2024-02-11 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('year', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IMUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('EIT', 'EIT'), ('TEACHING_FELLOW', 'TEACHING_FELLOW'), ('ADMIN_STAFF', 'ADMIN_STAFF'), ('ADMIN', 'ADMIN')], max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CohortMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cohort')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_cohort_members', to='users.imuser')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohorts', to='users.imuser')),
            ],
        ),
        migrations.AddField(
            model_name='cohort',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_cohorts', to='users.imuser'),
        ),
    ]