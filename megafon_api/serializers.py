from rest_framework import serializers

from megafon_api import models


class TariffSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        if data['start_date'] > data['exp_date']:
            raise serializers.ValidationError(
                'Expiration date can\'t be earlier than start date'
            )
        return data

    class Meta:
        model = models.Tariff
        fields = '__all__'
        read_only_fields = ('id', )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ('id', 'timestamp')
