from university.exceptions import ResourceException
from university.repositories import UserRepository
from university.serializers import StudentSerializer, TeacherSerializer, UserSerializer
from university.constants import USER_TYPE_STUDENT, USER_TYPE_TEACHER

class UserComponent:

    def get_all_users(self, user_type=None):
        if user_type == USER_TYPE_STUDENT:
            return UserRepository.get_students()
        elif user_type == USER_TYPE_TEACHER:
            return UserRepository.get_teachers()
        else:
            return UserRepository.get_all_users()

    def get_user_by_id(self, user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ResourceException(f"User with id {user_id} not found.")
        return user

    def get_serializer_class(self, user_type):
        if user_type == USER_TYPE_STUDENT:
            return StudentSerializer
        elif user_type == USER_TYPE_TEACHER:
            return TeacherSerializer
        return UserSerializer

    def create_user(self, serializer):
        serializer.save()

    def update_user_by_id(self, user_id, first_name, last_name):
        user = UserRepository.get_user_by_id(user_id=user_id)
        if not user:
            raise ResourceException(f"User with id {user_id} not found.")
        UserRepository.update_user_by_id(user_id=user_id, first_name = first_name,  last_name=last_name)


    def delete_user_by_id(self, user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ResourceException(f"User with id {user_id} not found.")
        user.delete()
        return True
