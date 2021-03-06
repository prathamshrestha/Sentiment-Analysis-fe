from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


#User serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=('id','first_name','last_name','username','email')

#Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','first_name','last_name','username','email','password')
        extra_kwargs={'password':{'write_only':True}}
    def create(self,validated_data):
        user=User.objects.create_user(validated_data['first_name'],validated_data['last_name'],validated_data['username'],validated_data['email'],validated_data['password'])
        return user


#login serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")