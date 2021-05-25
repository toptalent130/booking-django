from rest_framework import serializers

from .models import Listing, BookingInfo

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'listing_type', 'title', 'country', 'city', 'blocksday')
class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = ('id', 'blockdays_start', 'blockdays_end')