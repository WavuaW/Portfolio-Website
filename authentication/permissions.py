from rest_framework.permissions import BasePermission, SAFE_METHODS



class ShipmentCustomerOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user
    

class OwnerCustomPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user