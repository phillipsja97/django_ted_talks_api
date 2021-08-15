from django.conf.urls import url
from Talks import views

urlpatterns=[
    url(r'^alltalks$',views.TalksApi),
    url(r'^talk/([0-9]+)$',views.GetTalksById)
    # url(r'^gettalk/([0-9]+)$',views.GetTalksById)
]