from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Shipment, ShippingTo, ShippingFrom
from .serializers import (ShipmentSerializers, 
                        ShippingToSerializers, 
                        ShippingFromSerializers)


class ShipmentListView(APIView):
    """
    List all Transformers, or create a new Transformer
    """
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

  
    def get(self, request, format=None):
        transformers = Shipment.objects.all()
        serializer = ShipmentSerializers(transformers, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = ShipmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShipmentDetailView(APIView):
    	
	"""
	Retrieve, update or delete a transformer instance
	"""
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	
	def get_object(self, pk):
		# Returns an object instance that should
		# be used for detail views.
		try:
			return Shipment.objects.get(pk=pk)
		except Shipment.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		shipment = self.get_object(pk)
		serializer = ShipmentSerializers(shipment)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		shipment = self.get_object(pk)
		serializer = ShipmentSerializers(shipment, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		shipment = self.get_object(pk)
		shipment.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)