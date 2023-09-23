import face_recognition
from trip.models import Trip
from authentication.models import User

class ImageClassifier:
    '''
        Trip에 속한 image중에서 user image가 포함된 image를 반환
    '''
    def __init__(self,trip : Trip,user : User):
        self.user = user
        self.trip = trip

    def get_user_included_images(self):
        '''
            User 얼굴이 들어있는 Image만 반환 
        '''
        

