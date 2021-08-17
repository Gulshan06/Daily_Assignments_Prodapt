from seller.models import seller
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from seller.models import seller


class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model= seller
        fields = ('sname','sid','saddress','sphoneno')