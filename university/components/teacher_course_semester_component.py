from university.exceptions import ResourceException, DatabaseException
from university.models import TeacherCourseSemester
from university.repositories import TeacherCourseSemesterRepository

class TeacherCourseSemesterComponent:

    def get_all_teacher_course_semesters(self):
        return TeacherCourseSemesterRepository.get_all_teacher_course_semesters()

    def get_teacher_course_semester_by_id(self, teacher_course_semester_id):
        try:
            return TeacherCourseSemesterRepository.get_teacher_course_semester_by_id(teacher_course_semester_id)
        except TeacherCourseSemester.DoesNotExist:
            raise ResourceException(f"TeacherCourseSemester with id {teacher_course_semester_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error retrieving TeacherCourseSemester with id {teacher_course_semester_id}: {str(e)}")

    def create_teacher_course_semester(self, data):
        try:
            return TeacherCourseSemesterRepository.create_teacher_course_semester(data)
        except Exception as e:
            raise DatabaseException(f"Error creating TeacherCourseSemester: {str(e)}")

    def update_teacher_course_semester_by_id(self, teacher_course_semester_id, data):
        try:
            teacher_course_semester = TeacherCourseSemesterRepository.get_teacher_course_semester_by_id(teacher_course_semester_id)
            TeacherCourseSemesterRepository.update_teacher_course_semester(teacher_course_semester_id, **data)
        except TeacherCourseSemester.DoesNotExist:
            raise ResourceException(f"TeacherCourseSemester with id {teacher_course_semester_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error updating TeacherCourseSemester with id {teacher_course_semester_id}: {str(e)}")

    def delete_teacher_course_semester_by_id(self, teacher_course_semester_id):
        try:
            teacher_course_semester = TeacherCourseSemesterRepository.get_teacher_course_semester_by_id(teacher_course_semester_id)
            TeacherCourseSemesterRepository.delete_teacher_course_semester(teacher_course_semester)
        except TeacherCourseSemester.DoesNotExist:
            raise ResourceException(f"TeacherCourseSemester with id {teacher_course_semester_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error deleting TeacherCourseSemester with id {teacher_course_semester_id}: {str(e)}")
        return True
