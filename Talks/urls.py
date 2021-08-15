from django.conf.urls import url
from Talks import views

urlpatterns=[
    url(r'^alltalks$',views.AllTalks),
    url(r'^talk/([0-9]+)$',views.GetTalksById)
]