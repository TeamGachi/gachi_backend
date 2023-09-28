import face_recognition
from trip.models import Trip
from authentication.models import User
import cv2

class ImageClassifier:
    '''
        Trip에 속한 image중에서 user image가 포함된 image를 반환
    '''
    def __init__(self, trip : Trip ,user : User ):
        self.user = user
        self.trip = trip
        self.user_face = face_recognition.load_image_file(self.user.face_image)

    def is_user_included(self,trip_image):
        '''
            해당 image model에 user가 포함되어있는지 반환 
        '''
        target_image = face_recognition.load_image_file(trip_image.image)
        # 리사이징 
        small_frame = cv2.resize(target_image, (0, 0), fx=0.25, fy=0.25)
        # BGR to RGB 로 포매팅 변경 
        rgb_small_frame = small_frame[:, :, ::-1]
        # target 사진에서 모든 face 위치를 찾고 encoding 진행 
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.user_face, face_encoding)
            if True in matches:
                return True
        return False


    def get_user_included_images(self):
        '''
            Trip에서 User 얼굴이 들어있는 Image model만 반환 
        '''
        user_included_images = []
        trip_images = self.trip.objects.images.all()
        for trip_image in trip_images:
            if self.is_user_included(trip_image):
                user_included_images.append(trip_image)
        return user_included_images

    
        

