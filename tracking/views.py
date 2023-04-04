from .models import Tracking
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TrackingSerializer


class TrackingViews(APIView):
    def post(self, request):
        serializer = TrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['tracking_id'] = response.pop('id')
            response['shipment_id'] = response.pop('shipment')
            response['shipping_to_id'] = response.pop('shipping_to')
            response['shipping_from_id'] = response.pop('shipping_from')
            return Response({"status": "true", "tracking":response}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "true", "tracking": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, tracking_no):
        try:
            item = Tracking.objects.filter(tracking_no=tracking_no).first()
            serializer = TrackingSerializer(item)
            response = serializer.data
            response ['tracking_id']= serializer.data.get('id')
            response['shipment_id'] = serializer.data.get('shipment')
            response['shipping_to_id'] = serializer.data.get('shipping_to')
            response['shipping_from_id'] = serializer.data.get('shipping_from')
            print(response)
            return Response({"status": "true", "trackingJson": serializer.data}, status=status.HTTP_200_OK)
        except Tracking.DoesNotExist:
            return Response("Tracking Number is invalid or incorrect, status=status.HTT_404_NOT_FOUND")