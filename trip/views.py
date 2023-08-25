
from rest_framework import generics

# 여행 스케줄 CRUD

# 여행 생성 API
class TripMakeView(generics.CreateAPIView):
    pass

# 자신이 속한 여행 조회 API
class TripCheckView(generics.ListAPIView):
    pass

# 자신이 속한 여행 삭제 API 
class TripRemoveView(generics.RetrieveDestroyAPIView):
    pass
