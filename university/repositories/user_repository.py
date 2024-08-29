from university.models import User, Student, Teacher

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_students():
        return User.objects.filter(id__in=Student.objects.values_list('user_id', flat=True))

    @staticmethod
    def get_teachers():
        return User.objects.filter(id__in=Teacher.objects.values_list('user_id', flat=True))

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.get(pk=user_id)

    @staticmethod
    def create_user(user_data):
        user = User(**user_data)
        user.save()
        return user

    @staticmethod
    def update_user_by_id(user_id, first_name, last_name):
        user = User.objects.get(pk=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user

    @staticmethod
    def delete_user(user):
        user.delete()

    @staticmethod
    def get_total_students():
        return Student.objects.count()

    @staticmethod
    def get_total_teachers():
        return Teacher.objects.count()

    @staticmethod
    def get_total_users():
        return User.objects.count()
