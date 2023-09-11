from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import TripMembersOnly
from .serializer import TripSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import TripList

# 여행 생성 및 조회 
class TripView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    
    def get(self, request):
        ''' 
        자신이 속한 여행 조회
        '''
        user = request.user
        queryset = TripList(member=user)
        serialzier = TripSerializer(queryset)
        return Response(serialzier.data)
    
    def post(self, request):
        ''' 
        Trip 생성 
        '''
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid(): # trip member추가 
            serializer.save()
            tripmember = TripList.objects.create(trip=serializer.id,member=request.user)
            tripmember.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)


