from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import TripMembersOnly
from .serializer import TripSerializer,TripListSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import TripList,Trip

# 여행 생성 및 조회 
class TripView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def get(self, request):
        ''' 
            자신이 속한 Trip조회
        '''
        user = request.user
        queryset = TripList.objects.filter(member=user)
        serialzier = TripListSerializer(queryset,many=True) 
        return Response(serialzier.data)
    
    def post(self, request):
        ''' 
            새로운 Trip 생성 
        '''
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid(): # trip member추가 
            serializer.save()
            triplist = TripList.objects.create(trip=serializer.id,member=request.user)
            triplist.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self,request):
        '''
            특정 Trip 삭제 
        '''
        pass


# TripList 조회
class TripListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def get(self,request):
        pass
    
    def delete(self,request):
        '''
            특정 TripList에서 User가 포함된 튜플 삭제
        '''



# 특정 여행 세부사항 조회 
class TripDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def get(self,request,pk):
        try:
            trip_list = TripList.objects.get(id=pk)
            trip = Trip.objects.get(id=trip_list.trip)
            serializer = TripSerializer(trip)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

