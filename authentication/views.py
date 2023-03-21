from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.permissions import OwnerCustomPermission
from rest_framework.permissions import IsAuthenticated

from .models import (Shipment, 
                    ShippingTo, 
                    ShippingFrom,
                    Country,State,City)
from .serializers import (
    ShipmentSerializers,
    ShippingToSerializers,
    ShippingFromSerializers,
    CountrySerializer,CitySerializer,StateSerializer
)


class ShipmentListView(APIView):
    """
    List all shipment, or create a new shipment
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]


    def get(self, request, format=None):
        shipments = Shipment.objects.filter(user=request.user)

        serializer = ShipmentSerializers(instance=shipments, many=True)
        return Response(
            data={"message": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
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
        if request.user == shipment.user:
            serializer = ShipmentSerializers(instance=shipment)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"message": "It is not created by you"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk, format=None):
        shipment = self.get_object(pk)
        serializer = ShipmentSerializers(shipment, data=request.data)
        if request.user == shipment.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Can not update someone's post", status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        shipment = self.get_object(pk)
        if shipment.user == request.user:
            shipment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="Can't delete someone's post")


class ShippingToListView(APIView):
    """
    List all shippingto, or create a new shippingto
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]


    def get(self, request, format=None):
        shippingto = ShippingTo.objects.filter(user=request.user)

        serializer = ShippingToSerializers(instance=shippingto, many=True)
        return Response(
            data={"message": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

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
        if request.user == shippingto.user:
            serializer = ShippingToSerializers(instance=shippingto)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"message": "It is not created by you"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk, format=None):
        shippingto = self.get_object(pk)
        serializer = ShippingToSerializers(shippingto, data=request.data)
        if request.user == shippingto.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Can not update someone's post", status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        shippingto = self.get_object(pk)
        if shippingto.user == request.user:
            shippingto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="Can't delete someone's post")


class ShippingFromListView(APIView):
    """
    List all shippingfrom, or create a new shippingfrom
    """

    permission_classes = [IsAuthenticated, OwnerCustomPermission]

    def get(self, request, format=None):
        shippingfrom = ShippingFrom.objects.filter(user=request.user)

        serializer = ShippingFromSerializers(instance=shippingfrom, many=True)
        return Response(
            data={"message": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        serializer = ShippingFromSerializers(data=request.data)
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
        if request.user == shippingfrom.user:
            serializer = ShippingFromSerializers(instance=shippingfrom)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"message": "It is not created by you"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk, format=None):
        shippingfrom = self.get_object(pk)
        serializer = ShippingFromSerializers(shippingfrom, data=request.data)
        if request.user == shippingfrom.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Can not update someone's post", status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        shippingfrom = self.get_object(pk)
        if shippingfrom.user == request.user:
            shippingfrom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="Can't delete someone's post")
    

class CountryListView(GenericAPIView):
    """
    List all country
    """
    def get(self, request, format=None):
        state = Country.objects.all()

        serializer = CountrySerializer(state, many=True)
        return Response(
            data={"message": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    
class StateView(GenericAPIView):
    def get(self, request):
        """
        Get single state that is in a country
        """
        country_id = self.request.query_params.get('country')
        items = State.objects.filter(country=country_id)
        serializer = StateSerializer(items, many=True)
        return Response({"states": serializer.data}, status=status.HTTP_200_OK)


class CityView(GenericAPIView):
    def get(self, request):
        """
        Get single city that is in a state
        """
        state_id = self.request.query_params.get('state')
        items = City.objects.filter(country=state_id)
        serializer = CitySerializer(items, many=True)
        return Response({"cities": serializer.data}, status=status.HTTP_200_OK)      