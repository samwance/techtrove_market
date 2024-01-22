from rest_framework import serializers

from company_network.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt', 'created_at')
        read_only_fields = ('debt',)
