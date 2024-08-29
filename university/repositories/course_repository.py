from university.models import Course

class CourseRepository:

    @staticmethod
    def get_all_courses():
        return Course.objects.all()

    @staticmethod
    def get_course_by_id(course_id):
        return Course.objects.get(pk=course_id)

    @staticmethod
    def create_course(course_data):
        course = Course(**course_data)
        course.save()
        return course

    @staticmethod
    def update_course(course_id, **kwargs):
        course = Course.objects.get(pk=course_id)
        for key, value in kwargs.items():
            setattr(course, key, value)
        course.save()
        return course

    @staticmethod
    def delete_course(course):
        course.delete()

    @staticmethod
    def get_total_courses():
        return Course.objects.count()