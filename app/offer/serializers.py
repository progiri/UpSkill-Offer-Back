from rest_framework import serializers
from .models import *

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'title', 'salary', 'org', 'addr', 'desc', 'create_date')


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'fullname', 'github', 'phone', 'create_date')