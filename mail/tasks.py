import smtplib
from socket import error as SocketError
from celery import shared_task
from celery.contrib.abortable import AbortableTask
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Task,Attachment


@shared_task(bind=True, max_retries=None,base=AbortableTask)
def SendEmailTask(self,task_id):
    """
    Send an email as a Celery task.

    Args:
        self: The Celery task instance.
        task_id: The ID of the Task object in the database.

    Returns:
        str: A status message indicating success or failure.
    """
    task=Task.objects.get(id=task_id)
    print(f"Task ID: {self.request.id}")
    try:
        
        email = EmailMessage(
            task.mail.subject,
            task.mail.content,
            settings.EMAIL_HOST_USER,
            task.mail.receptors,
        )
        attachments = Attachment.objects.filter(mail_message=task.mail)
        for attachment in attachments:
            email.attach_file(attachment.attachments.path)
            
        email.send()
        task.finished_at = timezone.now()
        task.successfull = True
        task.is_proccessing = True
        task.save()
        return "Email sent successfully"

    except (Exception,smtplib.SMTPException, SocketError, TimeoutError, ConnectionRefusedError, smtplib.SMTPAuthenticationError,
            smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused, smtplib.SMTPDataError) as exc:
        task_exception_logs += str(exc)
        task.is_proccessing = True
        task.retry_count += 1
        task.successfull = False
        task.save()
        self.retry(exc=exc, countdown=1,max_retries=task.retry)
        return 'Email sending failed'