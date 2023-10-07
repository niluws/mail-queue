from celery.result import AsyncResult
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MailMessage
from .serializers import MailSerializers


class SendMailView(generics.CreateAPIView):
    """
    API view for sending mail messages.
    """
    queryset = MailMessage.objects.all()
    serializer_class = MailSerializers
    parser_classes = (MultiPartParser, FormParser)

class EmailView(generics.ListAPIView):
    """
    API view for listing mail messages.
    """
    queryset=MailMessage.objects.all()
    serializer_class=MailSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['receptors']

def cancel(request, task_id):
    """
    Cancel a task by task_id.

    Args:
        request: The HTTP request object.
        task_id: The ID of the task to cancel.

    Returns:
        JSON response indicating the result of the cancellation.
    """
    task = AsyncResult(task_id)
    print(task.state)
    if task.state == 'PENDING':
        
        task.revoke(terminate=True)
        return JsonResponse({'message': 'Task not started yet'})
    elif task.state in ['STARTED', 'RETRY']:
       
        task.revoke(terminate=True)
        return JsonResponse({'message': 'Canceled (Task was running)'})
    else:
        return JsonResponse({'message':  'Task already completed'})







