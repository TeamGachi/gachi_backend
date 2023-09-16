from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import TripMembersOnly
from .serializer import TripSerializer,TripListSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Trip

# 여행 생성 및 조회 
class TripView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def get(self, request):
        ''' 
            자신이 속한 Trip조회
        '''
        user = request.user
        queryset = Trip.objects.filter(members=user)
        serialzier = TripSerializer(queryset,many=True) 
        return Response(serialzier.data)
    
    def post(self, request):
        ''' 
            새로운 Trip 생성 
        '''
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid(): 
            trip = serializer.save()
            trip.members.add(request.user)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self,request):
        '''
            특정 Trip 삭제 
        '''
        pass

# 특정 여행 세부사항 조회 
class TripDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def get(self,request,pk):
        pass

