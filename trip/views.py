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

# 여행 생성 및 조회 
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
            자신이 속한 Trip조회
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
        GET POST 
        TripInvite 생성 및 조회 
        /api/trip/invite/
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    

class TrpInviteDeleteView(generics.DestroyAPIView):
    '''
        DELETE
        TripInvite 삭제
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        query = TripInvite.objects.get(id=self.kwargs['pk'])
        return query

class TripInviteAcceptView(generics.UpdateAPIView):
    '''
        PATCH 
        TripInvite 삭제 후 Trip의 User 필드에 user 추가  
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripInviteSerializer

    def update(self, request, *args, **kwargs):
        trip_invite = get_object_or_404(trip_invite,id=kwargs['pk'])
        trip = trip_invite.trip
        trip_invite.delete()
        trip.users.add(request.user)
        return Response(status=status.HTTP_200_OK)