from .models import User
from django.contrib.auth.password_validation import validate_password 

#serializer tools
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator

# 회원가입 시리얼라이저 클래스 
class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','password','password_again','gender','birth','username']
        
    email = serializers.EmailField( 
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())] # 유효성 검사 
    )

    password = serializers.CharField( 
        required = True,
        validators=[validate_password] 
    )
    password_again = serializers.CharField(
        write_only = True,
        required = True,
    )

    def validate(self,data):
        if data['password'] != data['password_again']:
            raise serializers.ValidationError(
                {"password":"비밀번호가 일치하지 않습니다."}
            )
        return data
    
    # json 데이터를 역직렬화하여 ORM에 저장 
    def create(self,validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            gender = validated_data['gender'],
            birth = validated_data['birth'],
            username= validated_data['username']
        )
        user.set_password(validated_data['password']) # 해싱하여 password저장 
        user.save() # 저장
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','password']
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    # Validating
    def validate(self,data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user) # 일치하는 유저의 토큰을 가져오기
            return token
        raise serializers.ValidationError(
            {"error":"unalbe to authentication"}
        )

