from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['id','username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, data):
        if data['password']!= data['password2']:
            raise serializers.ValidationError({'password':'Passwords does not match!'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(
            username=validated_data['username'],
            email= validated_data['email'],
            password=validated_data['password']
        )
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username']=user.username
        token['is_staff']=user.is_staff
        return token