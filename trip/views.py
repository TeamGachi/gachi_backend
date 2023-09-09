
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import json

# 여행 스케줄 CRUD
# 여행 생성 및 조회 API
class TripView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    ''' 
        자신이 속한 여행 조회
    '''
    def get(self, request):
        pass
    
    ''' 
        Trip session 생성 
    '''
    def post(self, request):
        pass


class TripDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        '''
            특정 여행에 대한 Detail 정보 반환 
        '''
        pass
    def post(self,request):
        '''
            특정 여행에 대한 Detail 정보 수정 
        '''
        pass
  