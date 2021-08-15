from rest_framework import serializers
from Talks.models import Talks

class TalksSerializer(serializers.ModelSerializer):
  class Meta:
    model=Talks
    fields=('talk_id', 'talk_title', 'talk_author', 'talk_href', 'talk_image')