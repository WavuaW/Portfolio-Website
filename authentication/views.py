from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.permissions import OwnerCustomPermission
from rest_framework.permissions import IsAuthenticated


from .models import Shipment, ShippingTo, ShippingFrom
from .serializers import (
    ShipmentSerializers,
    ShippingToSerializers,
    ShippingFromSerializers,
)


class ShipmentListView(GenericAPIView):
    """
    List all shipment, or create a new shipment
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]


    def get(self, request, format=None):
        shipments = Shipment.objects.all()
        for shipment in shipments:
            if request.user == shipment.user:
                serializer = ShipmentSerializers(instance=shipments, many=True)
                return Response(
                    data={"message": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"message": "authorized access"}, status=status.HTTP_403_FORBIDDEN
            )
        else:
            Response(
                data={"message": "Dont have a booking, create another"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, format=None):
        serializer = ShipmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipmentDetailView(GenericAPIView):

    """
    Retrieve, update or delete a shipment instance
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]

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
        if request.user == shipment.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Cant not updated someone post", status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        shipment = self.get_object(pk)
        if shipment.user == request.user:
            shipment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="Cant delete someone post")


class ShippingToListView(APIView):
    """
    List all shippingto, or create a new shippingto
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]

    def get(self, request, format=None):
        shippingto = ShippingTo.objects.all()
        serializer = ShippingToSerializers(shippingto, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShippingToSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShippingToDetailView(APIView):

    """
    Retrieve, update or delete a shippingto instance
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]

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
            serializer.save(user=request.user)
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

    permission_classes = [IsAuthenticated, OwnerCustomPermission]

    def get(self, request, format=None):
        shippingfrom = ShippingFrom.objects.all()
        serializer = ShippingFromSerializers(shippingfrom, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShippingToSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShippingFromDetailView(APIView):

    """
    Retrieve, update or delete a shippingto instance
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]

    def get_object(self, pk):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return ShippingFrom.objects.get(pk=pk)
        except ShippingFrom.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shippingfrom = self.get_object(pk)
        serializer = ShippingFromSerializers(shippingfrom)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        shippingfrom = self.get_object(pk)
        serializer = ShippingFromSerializers(shippingfrom, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shippingfrom = self.get_object(pk)
        shippingfrom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
