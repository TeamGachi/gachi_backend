from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..trip.permissions import TripMembersOnly

# 이미지 업로드 API
class ImageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def post(self,request):
        '''
            특정 Trip 세션에 이미지 업로드 
        '''
        pass
    def get(self,request):
        '''
            특정 Trip 세션의 모든 분류된 이미지 조회 
        '''
        pass


# 이미지 다운로드 API 
class ImageDownloadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [TripMembersOnly]
    def get(self,request):
        '''
            특정 Trip 세션의 특정 이미지 다운로드 
        '''
    pass

