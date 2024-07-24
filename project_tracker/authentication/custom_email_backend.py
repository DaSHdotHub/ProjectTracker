from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings

class CustomEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        kwargs['ssl_context'] = settings.EMAIL_SSL_CONTEXT
        super().__init__(*args, **kwargs)
