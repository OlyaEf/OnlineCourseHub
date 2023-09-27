from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    stripe = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'
