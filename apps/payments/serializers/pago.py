from rest_framework import serializers
from django.db import transaction

from payments.models import Pago
from orders.models import Pedido

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"

    def validate(self, data):
        pedido = data["pedido"]
        monto = data["monto"]

        if monto <= 0:
            raise serializers.ValidationError(
                "El monto del pago debe ser mayor a 0"
            )
        total_pago = pedido.total_pagado + monto

        if total_pago > pedido.total_neto:
            raise serializers.ValidationError(
                "El pago excede el total del pedido"
            )
        
        return data
    
    @transaction.atomic
    def create(self, validated_data):
        pago = pago.objects.create(**validated_data)

        pedido = pago.pedido
        pedido.total_pagado += pago.monto
        pedido.save()

        return pago