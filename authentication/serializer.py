from .models import User
from django.contrib.auth.password_validation import validate_password 
#serializer tools
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Registration 시리얼라이저 및 검증 
class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField( # 이메일 데이터 직렬화
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())] # 유효성 검사 
    )
    password = serializers.CharField( # 문자열 데이터 직렬화
        required = True,
        validators=[validate_password] # 일급객체
    )
    password_again = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = User
        fields = ['username','password','password_again','email']

    def validate(self,data):
        if data['password'] != data['password_again']:
            raise serializers.ValidationError(
                {"password":"비밀번호가 일치하지 않습니다."}
            )
        return data
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save() # 저장
        token = Token.objects.create(user=user)
        return user

