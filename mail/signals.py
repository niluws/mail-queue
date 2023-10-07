from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MailMessage, Task
from .tasks import SendEmailTask


@receiver(post_save, sender=MailMessage)
def create_mail_message(sender, instance, created, **kwargs):
    """
    Signal receiver to create a new task when a MailMessage instance is created.
    """
    if created:
       task = Task.objects.create(
            created_at=timezone.now(),
            is_proccessing=False,
            retry=30,
            retry_count=0,
            successfull=False,
            exception_logs='',
            mail=instance
        )


@receiver(post_save, sender=Task)
def create_mail_message(sender, instance, created, **kwargs):
    """
    Signal receiver to start processing a task when a Task instance is created.
    """
    if created:
       SendEmailTask.delay(
           instance.id
       )
       

