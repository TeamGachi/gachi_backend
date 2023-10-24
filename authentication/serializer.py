from .models import User
from django.contrib.auth.password_validation import validate_password 
#serializer tools
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

# 회원가입 시리얼라이저 클래스 
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["email","password","password_again","name","birth","gender","face_image"]


    email = serializers.EmailField( 
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())] 
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
                {"password":"비밀번호와 비밀번호 확인이 일치하지 않습니다."}
            )
        return data
  
    def create(self,validated_data):
        # User의 헬퍼 클래스 UserManager의 create_user 메소드 호출 
        user = User.objects.create_user(
            email=validated_data['email'],
            gender = validated_data['gender'],
            birth = validated_data['birth'],
            name= validated_data['name'],
            face_image = validated_data['face_image']
        )
        user.set_password(validated_data['password']) # 해싱하여 password저장 
        user.save() 
        return user

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','password']

    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    # email과 password검증 
    def validate(self,data):
        # model에서 해당하는 user가 존재하는지 검사 
        if len(data['password'])>=6 and len(data['password'])<=20 : # 비밀번호 길이검사
            return data 
        raise serializers.ValidationError(
            {"error":"unalbe to authentication"}
        )

