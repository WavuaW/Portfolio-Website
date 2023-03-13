from user.models import User
from rest_framework import serializers


# serializer for the user class
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=100, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    
    def create(self, validated_data):
        """
            description - create user 
        """
        password = validated_data.pop('password')           # remove the password to be hash
        user = super().create(validated_data)               # hash password
        user.set_password(password)                         # hash passord
        user.save()
        return user