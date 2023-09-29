from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import TripMembersOnly
from .serializer import TripSerializer,TripInviteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Trip,TripInvite

class TripView(APIView):
    '''
        GET POST DELETE
        여행 조회 , 여행 생성 , 여행 삭제 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]

    def get(self, request):
        ''' 
            /api/trip/
            user가 속한 Trip조회
        '''
        user = request.user
        queryset = Trip.objects.filter(users=user)
        serialzier = TripSerializer(queryset,many=True) 
        return Response(serialzier.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        ''' 
            /api/trip/
            새로운 Trip 생성 
        '''
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True): 
            trip = serializer.save()
            trip.users.add(request.user)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
    
    def patch(self,request,pk):
        '''
            /api/trip/<int:pk>
            pk를 가진 여행에서 user삭제 
        '''
        trip = Trip.objects.get(id=pk)
        trip.users.remove(request.user)
        # 모든 유저가 여행을 떠날시 해당 여행도 삭제 
        if trip.users.count()==0:
            trip.delete()
        return Response(status=status.HTTP_200_OK)


class TripInviteView(generics.CreateAPIView):
    '''
        POST 
        TripInvite 생성 및 자신에게 온 TripInvite 모두 조회 
        /api/trip/invite/
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TrpInviteHandleView(generics.RetrieveUpdateDestroyAPIView):
    '''
        GET PATCH DELETE
        특정 TripInvite 조회 수정 삭제 
        /api/trip/invite/<int:pk>/
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = TripInvite.objects.get(id=self.kwargs['pk'])
        return query

