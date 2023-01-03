from xml.dom import ValidationErr
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from api.models import Student
from restAuthApi.models import CustomUser
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class StudentModelSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']


class CustomUserRegistrationModelSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        # password = attrs.get('password')
        # password2 = attrs.get('password2')

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password does not match")
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class CustomUserLoginModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'created']


class UserChangePasswordModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user') # fetching user from context body in views
        if password != password2 :
            raise serializers.ValidationError("Password does not match")
        user.set_password(password)
        user.save()
        return attrs


class UserSendResetPasswordEmailModelSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')

        # check request user name match the database mail
        if CustomUser.objects.filter(email=email).exists():
            # fetch the user of that email in a database
            user = CustomUser.objects.get(email=email)
            print(user.name)

            # force_byted -> it will convert user id into byte stream
            # after then it will get convert into urlsafe_base64_encode
            uid = urlsafe_base64_encode(force_bytes(user.id))

            # it will generate token
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost:3000/rest_auth_api/reset/'+ uid + '/' + token
            print('Password reset link:  ', link)

            return attrs

        else:
            raise serializers.ValidationError('Email is not registered')


class UserPasswordResetConfirmModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 'password2']

    def validate(self, attrs):

        # try:
        password = attrs.get('password')
        password2 = attrs.get('password2')
        uid = self.context.get('uid')
        token = self.context.get('token')
        if password != password2:
            raise serializers.ValidationError("Password does not match")

        id = smart_str(urlsafe_base64_decode(uid)) # decode uid and it convert it into string
        user = CustomUser.objects.get(pk=id)

        if user is None:
            raise AuthenticationFailed('Invalid account. Please contant support')
        
        if not PasswordResetTokenGenerator().check_token(token, user):
            raise serializers.ValidationError('Token is not valid or expired')

        user.set_password(password)         
        user.save()
        return user
        # except DjangoUnicodeDecodeError as identifier:
        #     # it add extra security layer (optional)
        #     PasswordResetTokenGenerator().check_token(token, user)
        #     raise ValidationErr('Token is not valid or expired')

