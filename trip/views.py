from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import TripMembersOnly
from .serializer import TripSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
import os 

# 여행 생성 및 조회 
class TripView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]

    def get(self, request):
        ''' 
            자신이 속한 Trip조회
        '''
        user = request.user
        queryset = Trip.objects.filter(users=user)
        serialzier = TripSerializer(queryset,many=True) 
        return Response(serialzier.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        ''' 
            새로운 Trip 생성 
        '''
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True): 
            trip = serializer.save()
            trip.users.add(request.user)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        '''
            pk를 가진 여행에서 user삭제 
        '''
        trip = Trip.objects.get(id=pk)
        trip.users.remove(request.user)
        # users가 0명이라면 trip 자체도 삭제 
        if trip.users.count()== 0:
            # 해당 trip의 모든 사진요소 삭제 
            os.system(f"rm -rf ../media/{pk}")
            # 해당 trip 삭제 
            trip.delete()
        return Response(status=status.HTTP_200_OK)


    



