from django.conf import settings
from django.conf.urls import url
from .views import redirect

urlpatterns = [
    url(
        regex='^(?P<prefix>%s)(?P<tiny>\w+)$' % '|'.join(settings.SHORTEN_MODELS.keys()),
        view=redirect,
    )
]
