from django.conf.urls import url
from Talks import views

urlpatterns=[
    url(r'^talk$',views.TalksApi),
    url(r'^talk/([0-9]+)$',views.TalksApi)
]