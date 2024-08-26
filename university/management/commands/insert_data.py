from django.core.management.base import BaseCommand
from django.db import transaction
from university.models import (
    Role, User, Department, Course, CoursePrerequisite, Teacher,
    Student, UserRole, AcademicYear, Semester, TeacherCourseSemester,
    StudentTeacherCourseSemester, FeedbackCategory, Feedback
)

class Command(BaseCommand):
    help = 'Insert initial data into the database'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                # Insert Roles
                roles = [
                    {'code': 'ADMIN', 'name': 'Administrator'},
                    {'code': 'TEACHER', 'name': 'Teacher'},
                    {'code': 'STUDENT', 'name': 'Student'},
                    {'code': 'DEPT_HEAD', 'name': 'Department Head'},
                    {'code': 'REGISTRAR', 'name': 'Registrar'},
                ]
                Role.objects.bulk_create([Role(**role) for role in roles])

                # Insert Users
                users = [
                    {'first_name': 'Alice', 'last_name': 'Johnson', 'date_of_birth': '1980-05-14', 'email': 'alice.johnson@example.com', 'phone_number': '555-0101', 'address': '123 Elm St'},
                    {'first_name': 'Bob', 'last_name': 'Smith', 'date_of_birth': '1990-06-23', 'email': 'bob.smith@example.com', 'phone_number': '555-0102', 'address': '456 Oak St'},
                    {'first_name': 'Charlie', 'last_name': 'Brown', 'date_of_birth': '1995-07-30', 'email': 'charlie.brown@example.com', 'phone_number': '555-0103', 'address': '789 Pine St'},
                    {'first_name': 'David', 'last_name': 'Wilson', 'date_of_birth': '1985-08-10', 'email': 'david.wilson@example.com', 'phone_number': '555-0104', 'address': '321 Maple St'},
                    {'first_name': 'Emma', 'last_name': 'Davis', 'date_of_birth': '1992-11-22', 'email': 'emma.davis@example.com', 'phone_number': '555-0105', 'address': '654 Cedar St'},
                    {'first_name': 'Frank', 'last_name': 'Green', 'date_of_birth': '1988-03-12', 'email': 'frank.green@example.com', 'phone_number': '555-0106', 'address': '987 Spruce St'},
                    {'first_name': 'Grace', 'last_name': 'Hall', 'date_of_birth': '1991-09-05', 'email': 'grace.hall@example.com', 'phone_number': '555-0107', 'address': '876 Birch St'},
                    {'first_name': 'Hannah', 'last_name': 'White', 'date_of_birth': '1993-12-11', 'email': 'hannah.white@example.com', 'phone_number': '555-0108', 'address': '765 Redwood St'},
                    {'first_name': 'Ian', 'last_name': 'Lee', 'date_of_birth': '1994-07-25', 'email': 'ian.lee@example.com', 'phone_number': '555-0109', 'address': '654 Cypress St'},
                    {'first_name': 'Jane', 'last_name': 'King', 'date_of_birth': '1987-04-14', 'email': 'jane.king@example.com', 'phone_number': '555-0110', 'address': '543 Palm St'},
                ]
                User.objects.bulk_create([User(**user) for user in users])

                # Insert Departments
                departments = [
                    {'name': 'Computer Science', 'code': 'COMP_SCI', 'building': 'Engineering Building'},
                    {'name': 'Mathematics', 'code': 'MATH', 'building': 'Science Building'},
                    {'name': 'History', 'code': 'HIST', 'building': 'Humanities Building'},
                    {'name': 'Physics', 'code': 'PHYS', 'building': 'Physics Building'},
                    {'name': 'Chemistry', 'code': 'CHEM', 'building': 'Chemistry Building'},
                ]
                Department.objects.bulk_create([Department(**department) for department in departments])

                # Insert Courses
                courses = [
                    {'name': 'Introduction to Programming', 'code': 'CS101', 'credits': 3, 'department_id': 1},
                    {'name': 'Data Structures', 'code': 'CS102', 'credits': 4, 'department_id': 1},
                    {'name': 'Calculus I', 'code': 'MATH101', 'credits': 3, 'department_id': 2},
                    {'name': 'World History', 'code': 'HIST101', 'credits': 3, 'department_id': 3},
                    {'name': 'Physics I', 'code': 'PHYS101', 'credits': 4, 'department_id': 4},
                    {'name': 'Organic Chemistry', 'code': 'CHEM101', 'credits': 4, 'department_id': 5},
                ]
                Course.objects.bulk_create([Course(**course) for course in courses])

                # Insert Course Prerequisites
                CoursePrerequisite.objects.create(course_id=2, prerequisite_course_id=1)

                # Insert Teachers
                teachers = [
                    {'user_id': 2, 'department_id': 1},
                    {'user_id': 3, 'department_id': 2},
                    {'user_id': 6, 'department_id': 5},
                ]
                Teacher.objects.bulk_create([Teacher(**teacher) for teacher in teachers])

                # Insert Students
                students = [
                    {'user_id': 4, 'department_id': 1},
                    {'user_id': 5, 'department_id': 3},
                    {'user_id': 7, 'department_id': 2},
                    {'user_id': 8, 'department_id': 4},
                ]
                Student.objects.bulk_create([Student(**student) for student in students])

                # Insert User Roles
                user_roles = [
                    {'user_id': 1, 'role_id': 1},
                    {'user_id': 2, 'role_id': 2},
                    {'user_id': 3, 'role_id': 2},
                    {'user_id': 4, 'role_id': 3},
                    {'user_id': 5, 'role_id': 3},
                    {'user_id': 6, 'role_id': 2},
                    {'user_id': 7, 'role_id': 3},
                    {'user_id': 8, 'role_id': 3},
                    {'user_id': 9, 'role_id': 1},
                    {'user_id': 10, 'role_id': 4},
                ]
                UserRole.objects.bulk_create([UserRole(**user_role) for user_role in user_roles])

                # Insert Academic Years
                academic_years = [
                    {'start_from': '2024-01-01', 'end_at': '2024-12-31', 'description': 'Academic Year 2024'},
                    {'start_from': '2025-01-01', 'end_at': '2025-12-31', 'description': 'Academic Year 2025'},
                    {'start_from': '2023-01-01', 'end_at': '2023-12-31', 'description': 'Academic Year 2023'},
                ]
                AcademicYear.objects.bulk_create([AcademicYear(**year) for year in academic_years])

                # Insert Semesters
                semesters = [
                    {'name': 'Spring 2024', 'academic_year_id': 1},
                    {'name': 'Fall 2024', 'academic_year_id': 1},
                    {'name': 'Spring 2025', 'academic_year_id': 2},
                    {'name': 'Fall 2023', 'academic_year_id': 3},
                ]
                Semester.objects.bulk_create([Semester(**semester) for semester in semesters])

                # Insert Teacher Course Semester
                teacher_course_semesters = [
                    {'teacher_id': 1, 'course_id': 1, 'semester_id': 1},
                    {'teacher_id': 2, 'course_id': 3, 'semester_id': 1},
                    {'teacher_id': 2, 'course_id': 4, 'semester_id': 2},
                    {'teacher_id': 3, 'course_id': 6, 'semester_id': 4},
                ]
                TeacherCourseSemester.objects.bulk_create([TeacherCourseSemester(**record) for record in teacher_course_semesters])

                # Insert Student Teacher Course Semester
                student_teacher_course_semesters = [
                    {'student_id': 1, 'teacher_course_semester_id': 4, 'grade': 'A', 'status': 'Completed'},
                    {'student_id': 2, 'teacher_course_semester_id': 3, 'grade': 'B', 'status': 'Completed'},
                    {'student_id': 3, 'teacher_course_semester_id': 2, 'grade': 'A', 'status': 'Completed'},
                    {'student_id': 4, 'teacher_course_semester_id': 1, 'grade': 'B', 'status': 'Completed'},
                ]
                StudentTeacherCourseSemester.objects.bulk_create([StudentTeacherCourseSemester(**record) for record in student_teacher_course_semesters])

                # Insert Feedback Categories
                feedback_categories = [
                    {'name': 'Course Feedback', 'code': 'COURSE_FB'},
                    {'name': 'Teacher Feedback', 'code': 'TEACHER_FB'},
                    {'name': 'General Feedback', 'code': 'GENERAL_FB'},
                    {'name': 'Student Feedback', 'code': 'STUDENT_FB'},
                ]
                FeedbackCategory.objects.bulk_create([FeedbackCategory(**category) for category in feedback_categories])

                # Insert Feedback
                feedback = [
                    {'user_id': 1, 'teacher_course_semester_id': 1, 'comment': 'Great course!', 'feedback_category_id': 1},
                    {'user_id': 2, 'teacher_course_semester_id': 2, 'comment': 'Very informative!', 'feedback_category_id': 2},
                    {'user_id': 3, 'teacher_course_semester_id': 3, 'comment': 'Excellent coverage of material!', 'feedback_category_id': 3},
                    {'user_id': 4, 'teacher_course_semester_id': 4, 'comment': 'Challenging but rewarding!', 'feedback_category_id': 4},
                    {'user_id': 1, 'teacher_course_semester_id': 1, 'comment': 'Amazing course!', 'feedback_category_id': 1},
                    {'user_id': 2, 'teacher_course_semester_id': 1, 'comment': 'Bad course!', 'feedback_category_id': 2},
                    {'user_id': 3, 'teacher_course_semester_id': 3, 'comment': 'Excellent coverage of material!', 'feedback_category_id': 3},
                    {'user_id': 4, 'teacher_course_semester_id': 4, 'comment': 'Challenging but rewarding!', 'feedback_category_id': 4},
                ]
                Feedback.objects.bulk_create([Feedback(**fb) for fb in feedback])

                self.stdout.write(self.style.SUCCESS('Successfully inserted data into the database.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {str(e)}'))
            raise e