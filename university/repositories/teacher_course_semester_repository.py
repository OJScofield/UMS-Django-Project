from university.models import TeacherCourseSemester

class TeacherCourseSemesterRepository:

    @staticmethod
    def get_all_teacher_course_semesters():
        return TeacherCourseSemester.objects.all()

    @staticmethod
    def get_teacher_course_semester_by_id(teacher_course_semester_id):
        return TeacherCourseSemester.objects.get(pk=teacher_course_semester_id)

    @staticmethod
    def create_teacher_course_semester(data):
        teacher_course_semester = TeacherCourseSemester(**data)
        teacher_course_semester.save()
        return teacher_course_semester

    @staticmethod
    def update_teacher_course_semester(teacher_course_semester_id, **kwargs):
        teacher_course_semester = TeacherCourseSemester.objects.get(pk=teacher_course_semester_id)
        for key, value in kwargs.items():
            setattr(teacher_course_semester, key, value)
        teacher_course_semester.save()
        return teacher_course_semester

    @staticmethod
    def delete_teacher_course_semester(teacher_course_semester):
        teacher_course_semester.delete()
