from rest_framework import serializers
from .models import info


class infoSerializer(serializers.ModelSerializer):

    class Meta:
        model=info
        fields='__all__'
