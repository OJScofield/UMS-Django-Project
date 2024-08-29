from university.exceptions import ResourceException, DatabaseException
from university.models import Course
from university.repositories import CourseRepository

class CourseComponent:

    def get_all_courses(self):
        return CourseRepository.get_all_courses()

    def get_course_by_id(self, course_id):
        try:
            return CourseRepository.get_course_by_id(course_id)
        except Course.DoesNotExist:
            raise ResourceException(f"Course with id {course_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error retrieving course with id {course_id}: {str(e)}")

    def create_course(self, course_data):
        try:
            return CourseRepository.create_course(course_data)
        except Exception as e:
            raise DatabaseException(f"Error creating course: {str(e)}")

    def update_course_by_id(self, course_id, data):
        try:
            course = CourseRepository.get_course_by_id(course_id)
            CourseRepository.update_course(course_id, **data)
        except Course.DoesNotExist:
            raise ResourceException(f"Course with id {course_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error updating course with id {course_id}: {str(e)}")

    def delete_course_by_id(self, course_id):
        try:
            course = CourseRepository.get_course_by_id(course_id)
            CourseRepository.delete_course(course)
        except Course.DoesNotExist:
            raise ResourceException(f"Course with id {course_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error deleting course with id {course_id}: {str(e)}")
        return True
