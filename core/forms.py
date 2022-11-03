from django import forms

from core.models import NotificationHistory


class NotificationHistoryForm(forms.ModelForm):
    class Meta:
        model = NotificationHistory
        fields = '__all__'