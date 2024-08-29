from university.exceptions import ResourceException, DatabaseException
from university.models import User
from university.repositories import UserRepository
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
        try:
            user = UserRepository.get_user_by_id(user_id)
            return user
        except User.DoesNotExist:
            raise ResourceException(f"User with id {user_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error retrieving user with id {user_id}: {str(e)}")

    def create_user(self, user_data):
        try:
            return UserRepository.create_user(user_data)
        except Exception as e:
            raise DatabaseException(f"Error creating user: {str(e)}")

    def update_user_by_id(self, user_id, first_name, last_name):
        try:
            user = UserRepository.get_user_by_id(user_id=user_id)
            UserRepository.update_user_by_id(user_id=user_id, first_name=first_name, last_name=last_name)
        except User.DoesNotExist:
            raise ResourceException(f"User with id {user_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error updating user with id {user_id}: {str(e)}")

    def delete_user_by_id(self, user_id):
        try:
            user = UserRepository.get_user_by_id(user_id)
            UserRepository.delete_user(user)
        except User.DoesNotExist:
            raise ResourceException(f"User with id {user_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error deleting user with id {user_id}: {str(e)}")

    def get_total_students(self):
        return UserRepository.get_total_students()

    def get_total_teachers(self):
        return UserRepository.get_total_teachers()

    def get_total_users(self):
        return UserRepository.get_total_users()