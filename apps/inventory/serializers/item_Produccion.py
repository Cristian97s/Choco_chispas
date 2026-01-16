from rest_framework import serializers
from inventory.models import ItemProduccion

class ItemProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemProduccion
        fields = "__all__"