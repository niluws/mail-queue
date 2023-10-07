from rest_framework import serializers
from .models import MailMessage,Task,Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class MailSerializers(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    uploaded_file = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    class Meta:
        model = MailMessage
        fields = ['subject','receptors','content','attachments','uploaded_file']

    def create(self, validated_data):
        uploaded_file= validated_data.pop("uploaded_file")
        mail_message = MailMessage.objects.create(**validated_data)
        for attachments in uploaded_file:
            Attachment.objects.create(mail_message=mail_message, attachments=attachments)
        return mail_message
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
