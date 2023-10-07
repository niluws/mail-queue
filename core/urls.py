from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mail import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("email/", views.SendMailView.as_view()),
    path('email-list/',views.EmailView.as_view()),
    path('cancel/<str:task_id>/', views.cancel),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
