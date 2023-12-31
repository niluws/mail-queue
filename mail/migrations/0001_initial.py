# Generated by Django 4.2.5 on 2023-09-30 20:30

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('receptors', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=50), size=None)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('retry', models.IntegerField()),
                ('retry_count', models.IntegerField(default=0)),
                ('is_proccessing', models.BooleanField()),
                ('successfull', models.BooleanField()),
                ('exception_logs', models.CharField(max_length=200)),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.mailmessage')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('mail_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='mail.mailmessage')),
            ],
        ),
    ]
