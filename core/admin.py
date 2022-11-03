from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from core.models import NotificationHistory
# Register your models here.

@admin.register(NotificationHistory)
class NotificationHistoryAdmin(admin.ModelAdmin):
    model = NotificationHistory
    formfield_overrides = {models.TextField: {'widget': CKEditorWidget}}