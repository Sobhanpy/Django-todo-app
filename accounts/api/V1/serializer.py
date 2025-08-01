from accounts.models import CustomeUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=10 , write_only=True)
    class Meta:
        model = CustomeUser
        fields = [
            "email", "username", "password", "password1"]

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password1')

        if password1 != password2:
            raise serializers.ValidationError({
                'detail':'password dose not confirmed'})  
        try:

            validate_password(password1)

        except exceptions.ValidationError as v:

            raise serializers.ValidationError({
                'detail':list(v.messages)
            }) 
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1', None)
        return CustomeUser.objects.create_user(**validated_data)


class CustomeAuthTokenSerializer(serializers.Serializer):
        email = serializers.EmailField(
        label=("Email"),
        write_only=True
    )
        password = serializers.CharField(
            label=("Password"),
            style={'input_type': 'password'},
            trim_whitespace=False,
            write_only=True
        )
        token = serializers.CharField(
            label=("Token"),
            read_only=True
        )

        def validate(self, attrs):
            email = attrs.get('email')
            password = attrs.get('password')

            if email and password:
                user = authenticate(request=self.context.get('request'),
                                    email=email, password=password)
                if not user:
                    msg = ('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = ('Must include "email" and "password".')
                raise serializers.ValidationError(msg, code='authorization')
            attrs['user'] = user
            return attrs

                                      