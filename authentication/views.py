from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.permissions import ShipmentCustomerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Shipment, ShippingTo, ShippingFrom
from .serializers import (ShipmentSerializers, 
                        ShippingToSerializers, 
                        ShippingFromSerializers)


class ShipmentListView(APIView):
    """
    List all shipment, or create a new shipment
    """
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,ShipmentCustomerOrReadOnly]

  
    def get(self, request, format=None):
        shipment = Shipment.objects.all()
        serializer = ShipmentSerializers(shipment , many=True)
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
	Retrieve, update or delete a shipment instance
	"""
	authentication_classes=[TokenAuthentication]
	permission_classes=[ShipmentCustomerOrReadOnly]
	
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



class ShippingToListView(APIView):
    """
    List all shippingto, or create a new shippingto
    """
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, ShipmentCustomerOrReadOnly]

  
    def get(self, request, format=None):
        shippingto = ShippingTo.objects.all()
        serializer = ShippingToSerializers(shippingto, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = ShippingToSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShippingToDetailView(APIView):
    	
	"""
	Retrieve, update or delete a shippingto instance
	"""
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated, ShipmentCustomerOrReadOnly]
	
	def get_object(self, pk):
		# Returns an object instance that should
		# be used for detail views.
		try:
			return ShippingTo.objects.get(pk=pk)
		except ShippingTo.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		shippingto = self.get_object(pk)
		serializer = ShippingToSerializers(shippingto)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		shippingto = self.get_object(pk)
		serializer = ShippingToSerializers(shippingto, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		shippingto = self.get_object(pk)
		shippingto.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	

class ShippingFromListView(APIView):
    """
    List all shippingto, or create a new shippingto
    """
    #authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, ShipmentCustomerOrReadOnly]

  
    def get(self, request, format=None):
        shippingfrom = ShippingFrom.objects.all()
        serializer = ShippingFromSerializers(shippingfrom , many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = ShippingToSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShippingFromDetailView(APIView):
    	
	"""
	Retrieve, update or delete a shippingto instance
	"""
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated, ShipmentCustomerOrReadOnly]
	
	def get_object(self, pk):
		# Returns an object instance that should
		# be used for detail views.
		try:
			return ShippingFrom.objects.get(pk=pk)
		except ShippingFrom.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		shippingfrom  = self.get_object(pk)
		serializer = ShippingFromSerializers(shippingfrom )
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		shippingfrom  = self.get_object(pk)
		serializer = ShippingFromSerializers(shippingfrom , data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		shippingfrom = self.get_object(pk)
		shippingfrom .delete()
		return Response(status=status.HTTP_204_NO_CONTENT)