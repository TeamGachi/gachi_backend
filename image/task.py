
from celery import shared_task
import face_recognition
from trip.models import Trip
from authentication.models import User
from django.conf import settings
import cv2
from config import ENV
from image.models import TripImage

@shared_task
def get_images():
    pass

class ImageClassifier:
    '''
        Trip에 속한 image중에서 user image가 포함된 image를 반환
    '''
    def __init__(self, trip : Trip ,user : User ):
        self.user = user
        self.trip = trip


    def is_user_included(self,trip_image : TripImage):
        '''
            해당 image model에 user가 포함되어있는지 반환 
        '''
        media_base_url = settings.MEDIA_URL
        user_image = face_recognition.load_image_file("."+media_base_url+str(self.user.face_image))
        target_image = face_recognition.load_image_file("."+media_base_url+str(trip_image.image))
        # 리사이징 
        small_frame = cv2.resize(target_image, (0, 0), fx=0.25, fy=0.25)
        # BGR to RGB 로 포매팅 변경 
        rgb_small_frame = small_frame[:, :, ::-1]
        # target 사진에서 모든 face 위치를 찾고 encoding 진행 
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(user_image, face_encoding)
            if True in matches:
                return True
        return False

    @shared_task
    def get_user_included_images(self):
        '''
            Trip에서 User 얼굴이 들어있는 Image model만 반환 
        '''
        user_included_images = []
        trip_images = self.trip.images.all() # Trip을 참조하고 있는 image 모델 인스턴스 queryset 
        for trip_image in trip_images:
            if self.is_user_included(trip_image):
                user_included_images.append(trip_image)
        return user_included_images