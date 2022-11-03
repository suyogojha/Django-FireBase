from django.shortcuts import render
from django.views.generic import View

from fcm_django.models import FCMDevice

from core.models import NotificationHistory

from core.forms import NotificationHistoryForm
# Create your views here.

class IndexView(View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class NotificationView(View):
    template_name = 'core/notification_form.html'
    form_class = NotificationHistoryForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            context = {'form': self.form_class()}
        else:
            context = {'form': form}

        fcm_token = form.instance.fcm_token
        notification_body = form.instance.body
        notification_title = form.instance.title
        notification_icon = form.instance.icon
        notification_image = form.instance.image

        notification_icon_url = request.build_absolute_uri(notification_icon.url) if notification_icon else ''
        notification_image_url = request.build_absolute_uri(notification_image.url) if notification_image else ''

        devices = FCMDevice.objects.filter(
            registration_id=fcm_token
            )

        devices.send_message(
            title=notification_title, 
            body=notification_body, 
            icon=notification_icon_url, 
            data={
                "image": notification_image_url,
            }
        )

        return render(request, self.template_name, context)