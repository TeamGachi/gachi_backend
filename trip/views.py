from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from .serializer import TripSerializer,TripInviteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Trip,TripInvite
from permissions import TripMembersOnly

class TripView(generics.ListCreateAPIView):
    '''
        GET POST 
        /api/trip/
        User가 속한 여행 조회 , User가 여행 생성 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Trip.objects.filter(users=user)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            trip = serializer.save()
            trip.users.add(request.user)
        else:
            return Response(data={"message" : "유효하지 않은 정보입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    

class TripUpdateView(generics.RetrieveUpdateAPIView):
    '''
        /api/trip/<int:pk>/
        PK 여행 레코드에서 User를 제외 (여행탈퇴)
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]

    def update(self, request, *args, **kwargs):

        action = request.data.get('action')

        if action == "withdraw":
            trip = get_object_or_404(Trip,id=kwargs['pk'])
            trip.users.remove(request.user)
            # 모든 유저가 여행을 떠날시 해당 여행도 삭제 
            if trip.users.count()==0:
                trip.delete()
            return Response({"message" : "여행에서 User가 제거되었습니다."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message" : "올바르지 않은 입력입니다."},
                            status=status.HTTP_400_BAD_REQUEST)



class TripInviteView(generics.ListCreateAPIView):
    '''
        GET POST 
        TripInvite 생성 및 자신에게 온 TripInvite 모두 조회 
        /api/trip/invite/
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripInviteSerializer

    def get_queryset(self):
        queryset = TripInvite.objects.filter(receiver=self.request.user)
        return queryset
    

    
class TrpInviteUpdateView(generics.UpdateAPIView):
    '''
        PATCH 
        TripInvite 거절 및 수락 
        /api/trip/invite/<int:pk>/
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self,request,*args,**kwargs):
        trip_invite = get_object_or_404(TripInvite,
                                        id=kwargs['pk'])
        action = request.data.get('action')
   
        data = {"message": "" }
        if action == "accept":
            trip = trip_invite.trip
            trip.users.add(request.user)
            trip_invite.delete()
            data["message"] = "초대를 수락하였습니다."
        elif action == "reject":
            trip_invite.delete()
            data["message"] = "초대를 거절하였습니다."
        else:
            data["message"] = "올바르지 않은 입력입니다."
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data,status=status.HTTP_200_OK)

 
