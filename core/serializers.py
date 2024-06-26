from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    assword2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'phone_number', 'email_verified']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does not match"})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exists"})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account


class MessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField()

    class Meta:
        model = User
        fields = ('message',)


class ResponseSerializer(serializers.ModelSerializer):
    response = serializers.CharField()

    class Meta:
        model = User
        fields = ('response',)

   
        