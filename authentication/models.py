from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,name,gender,birth,password=None,face_image=None):
        if not email:
            raise ValueError("유저 이메일이 존재하지 않습니다.")
        if not name:
            raise ValueError("유저 이름이 존재하지 않습니다.")
        user = self.model(
            email = self.normalize_email(email), # 이메일 정규화 
            name = name,
            gender = gender,
            birth = birth,
            face_image=face_image
        )
        user.set_password(password) # 암호 난독화
        user.save()
        return user 
    
    def create_superuser(self,email,name="lim",gender="남자",birth="1999-08-22",password=None):
        user = self.create_user(
            email = self.normalize_email(email), # 이메일 정규화 
            name = name,
            gender = gender,
            birth = birth,
        )
        user.set_password(password) # 암호 난독화
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser):
    # id와 password만 AbstractBaseUser에 존재 
    email = models.CharField(primary_key=True, max_length=50) 
    name = models.CharField(max_length=50)
    birth = models.DateField()
    gender = models.CharField(max_length=20)
    face_image = models.ImageField(upload_to="faces/")
    # AbstractUser 필수 필드 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    # CustomUser 매니저 클래스 지정 
    objects = UserManager() 
    # username filed 지정 
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "authentication_user"



    
    
