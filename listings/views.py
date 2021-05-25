import json
from django.core.serializers import serialize
from rest_framework.response import Response
from .serializers import ListingSerializer, BookingInfoSerializer
from .models import Listing, BookingInfo
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.http import JsonResponse
from datetime import datetime

class ListingView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get(self, request, *args, **kwargs):
    
        Listings = Listing.objects.all()
        BookingInfos = BookingInfo.objects.all()
        JsonListings = json.loads(serialize("json", Listings))
        
        data = []
        check_in = request.GET['check_in']
        check_out = request.GET['check_out']
        max_price = request.GET['max_price']

        for each in BookingInfos:
            for obj in JsonListings:
                if each.id == obj["fields"]["blocksday"]:
                    # datetime.strptime(obj["fields"]["blockdays_start"], "%Y-%m-%d").strftime("%d-%m-%Y")
                    if int(max_price) >= int(each.price):
                        data.append({"listing_type": obj["fields"]["listing_type"],
                                    "title": obj["fields"]["title"],
                                    "country": obj["fields"]["country"],
                                    "city": obj["fields"]["city"],
                                    "price": each.price })
        data = sorted(data, key=lambda k: int(k['price']), reverse=False)

        return JsonResponse({"items": data},  content_type='application/json')
        # return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class ListingDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)