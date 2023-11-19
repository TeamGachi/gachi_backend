from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializer import TripImageSerializer, FaceImageSerializer
from .models import TripImage
from django.shortcuts import get_object_or_404
from permissions import TripMembersOnly
from .task import *
from authentication.models import User


class ImageCreateView(generics.CreateAPIView):
    """
    POST
    /api/image/
    TripImage생성 VIEW
    """

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = TripImageSerializer

    def get(self, request):
        """
        GET
        /api/iamge/?{email}
        email에 해당하는 유저의 이미지 반환
        """
        try:
            email = request.query_params["email"]
        except:
            return Response(
                {"message": "이메일 쿼리스트링을 넣어주세요"}, status.HTTP_400_BAD_REQUEST
            )
        user = get_object_or_404(User, email=email)
        serializer = FaceImageSerializer(user)
        return Response(serializer.data)
        if user.face_image:
            image_path = user.face_image.path
            with open(image_path, "rb") as image_file:
                return FileResponse(image_file, content_type="image/jpeg")
        else:
            return Response({"message": "얼굴 이미지가 없습니다."}, status.HTTP_404_NOT_FOUND)


class ImageListView(generics.ListAPIView):
    """
    GET
    /api/image/<int:pk>/?email
    Trip중 PK를 가지고 있는 Trip에 속하는 모든 이미지 조회 요청 VIEW
    """

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [TripMembersOnly]
    serializer_class = TripImageSerializer

    def get_queryset(self):
        queryset = TripImage.objects.filter(trip=self.kwargs["pk"])
        return queryset

    def list(self, request, *args, **kwargs):
        email = self.request.GET.get("email", None)
        if email is None:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = self.get_queryset()
            user = get_object_or_404(User, email=email)
            try:
                result = get_user_included_images(user, queryset)
            except IndexError:
                return Response(
                    {"message": "유저의 아이디에 등록된 사진에 얼굴이 들어있지 않습니다."},
                    status.HTTP_400_BAD_REQUEST,
                )
            serializer = self.get_serializer(result, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
