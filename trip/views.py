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
            자신이 속한 Trip 조회
        '''
        user = request.user
        queryset = TripList.objects.filter(member=user)
        trips = [query.trip for query in queryset] # User가 속한 모든 Trip의 list 
        serialzier = TripSerializer(trips,many=True) # 모든 쿼리셋을 직렬화 
        return Response(serialzier.data)
    
    def post(self, request):
        ''' 
            Trip 생성 
        '''
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid(): # trip member추가 
            serializer.save()
            triplist = TripList.objects.create(trip=serializer.id,member=request.user)
            triplist.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

# 특정 여행 세부 정보 조회 
class TripDetailView(APIView):
    def get(self,request,pk):
        pass
