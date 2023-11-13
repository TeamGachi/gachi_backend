import face_recognition


def get_user_included_images(user, queryset):
    """
    input : User 모델 , TripImage 모델 queryset
    output : 분류된 TripImage queryset
    """
    user_included_images = []
    user_image = face_recognition.load_image_file(user.face_image)
    for trip_image in queryset:
        unknown_image = face_recognition.load_image_file(trip_image.image)
        try:
            user_face_encoding = face_recognition.face_encodings(
                user_image, num_jitters=100
            )[0]
            unknown_face_encodings = face_recognition.face_encodings(
                unknown_image, num_jitters=100
            )
        except IndexError:
            return "error"

        known_faces = [user_face_encoding]

        for unknown_face_encoding in unknown_face_encodings:
            results = face_recognition.compare_faces(
                known_faces, unknown_face_encoding, tolerance=0.4
            )
            if True in results:
                user_included_images.append(trip_image)
                break

    return user_included_images
