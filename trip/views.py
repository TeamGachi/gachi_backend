
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
        { 
            'place' , 'department' , 'arrival' 
        }
    '''
    def get(self, request):
        return "hi"
    
    ''' 
        Generating Trip session  
    '''
    def post(self, request):
        data = {
            "place": json.loads(request.data.get("place")),
            "department": json.loads(request.data.get("departing_date")),
            "arrival": json.loads(request.data.get("arriving_date")),
        }
        return "d"



''' 특정 Trip에 대한 detail 정보 반환 '''
class TripDetailView(APIView):
    pass
  