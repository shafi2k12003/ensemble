
from django.conf.urls import url
from rest_framework import routers
from ensemble_api.views import genesView

router = routers.DefaultRouter()



urlpatterns = [
    url(r'genes', genesView),
]

urlpatterns += router.urls
