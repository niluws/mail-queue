from django.db import models
from django.contrib.postgres.fields import ArrayField


class MailMessage(models.Model):
    subject=models.CharField(max_length=100)
    receptors=ArrayField(models.EmailField(max_length=50))
    content=models.CharField(max_length=100)

class Attachment(models.Model):
    mail_message = models.ForeignKey(MailMessage, related_name='attachments', on_delete=models.CASCADE)
    attachments = models.FileField(upload_to='attachments/',blank=True,null=True)

class Task(models.Model):
    mail=models.ForeignKey(MailMessage,on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    finished_at=models.DateTimeField(null=True,blank=True)
    retry=models.IntegerField()
    retry_count=models.IntegerField(default=0)
    is_proccessing=models.BooleanField()
    successfull=models.BooleanField()
    exception_logs=models.CharField(max_length=200)

