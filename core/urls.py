from django.urls import path
from core.views import (
    IndexView,
    NotificationView
)


urlpatterns = [
    path('', IndexView.as_view()),
    path('notify/', NotificationView.as_view()),
]
