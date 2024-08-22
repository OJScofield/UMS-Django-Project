from university.models import AcademicYear, Course, Department, Semester, User, Student, Teacher, StudentTeacherCourseSemester, TeacherCourseSemester
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Inserts initial data into the database'

    def handle(self, *args, **kwargs):
        # Insert into AcademicYear
        academic_year_2024 = AcademicYear.objects.create(start_from='2024-01-01', end_at='2024-12-31',
                                                         description='Academic Year 2024')
        academic_year_2025 = AcademicYear.objects.create(start_from='2025-01-01', end_at='2025-12-31',
                                                         description='Academic Year 2025')
        academic_year_2023 = AcademicYear.objects.create(start_from='2023-01-01', end_at='2023-12-31',
                                                         description='Academic Year 2023')

        # Insert into Department
        department_cs = Department.objects.create(name='Computer Engineering', building='Engineering Building')
        department_math = Department.objects.create(name='Mathematics', building='Math Building')
        department_history = Department.objects.create(name='History', building='History Building')
        department_physics = Department.objects.create(name='Physics', building='Physics Building')
        department_chemistry = Department.objects.create(name='Chemistry', building='Chemistry Building')

        # Insert into Course
        course_cs101 = Course.objects.create(name='Introduction to Programming', code='CS101', credits=3,
                                             department=department_cs)
        course_cs102 = Course.objects.create(name='Data Structures', code='CS102', credits=4, department=department_cs)
        course_math101 = Course.objects.create(name='Calculus I', code='MATH101', credits=3, department=department_math)
        course_hist101 = Course.objects.create(name='World History', code='HIST101', credits=3,
                                               department=department_history)
        course_phys101 = Course.objects.create(name='Physics I', code='PHYS101', credits=4,
                                               department=department_physics)
        course_chem101 = Course.objects.create(name='Organic Chemistry', code='CHEM101', credits=4,
                                               department=department_chemistry)

        # Insert into User
        user_alice = User.objects.create(first_name='Alice', last_name='Johnson', date_of_birth='1980-05-14',
                                         email='alice.johnson@example.com', phone_number='555-0101',
                                         address='123 Elm St')
        user_bob = User.objects.create(first_name='Bob', last_name='Smith', date_of_birth='1990-06-23',
                                       email='bob.smith@example.com', phone_number='555-0102', address='456 Oak St')
        user_charlie = User.objects.create(first_name='Charlie', last_name='Brown', date_of_birth='1995-07-30',
                                           email='charlie.brown@example.com', phone_number='555-0103',
                                           address='789 Pine St')
        user_david = User.objects.create(first_name='David', last_name='Wilson', date_of_birth='1985-08-10',
                                         email='david.wilson@example.com', phone_number='555-0104',
                                         address='321 Maple St')
        user_emma = User.objects.create(first_name='Emma', last_name='Davis', date_of_birth='1992-11-22',
                                        email='emma.davis@example.com', phone_number='555-0105', address='654 Cedar St')
        user_frank = User.objects.create(first_name='Frank', last_name='Green', date_of_birth='1988-03-12',
                                         email='frank.green@example.com', phone_number='555-0106',
                                         address='987 Spruce St')
        user_grace = User.objects.create(first_name='Grace', last_name='Hall', date_of_birth='1991-09-05',
                                         email='grace.hall@example.com', phone_number='555-0107',
                                         address='876 Birch St')
        user_hannah = User.objects.create(first_name='Hannah', last_name='White', date_of_birth='1993-12-11',
                                          email='hannah.white@example.com', phone_number='555-0108',
                                          address='765 Redwood St')
        user_ian = User.objects.create(first_name='Ian', last_name='Lee', date_of_birth='1994-07-25',
                                       email='ian.lee@example.com', phone_number='555-0109', address='654 Cypress St')
        user_jane = User.objects.create(first_name='Jane', last_name='King', date_of_birth='1987-04-14',
                                        email='jane.king@example.com', phone_number='555-0110', address='543 Palm St')

        # Insert into Student
        student_david = Student.objects.create(user=user_david,
                                               department=department_cs)  # David Wilson is a student in the Computer Science department
        student_emma = Student.objects.create(user=user_emma,
                                              department=department_history)  # Emma Davis is a student in the History department
        student_grace = Student.objects.create(user=user_grace,
                                               department=department_math)  # Grace Hall is a student in the Mathematics department
        student_hannah = Student.objects.create(user=user_hannah,
                                                department=department_physics)  # Hannah White is a student in the Physics department

        # Insert into Teacher
        teacher_bob = Teacher.objects.create(user=user_bob,
                                             department=department_cs)  # Bob Smith teaches in the Computer Science department
        teacher_charlie = Teacher.objects.create(user=user_charlie,
                                                 department=department_math)  # Charlie Brown teaches in the Mathematics department
        teacher_frank = Teacher.objects.create(user=user_frank,
                                               department=department_chemistry)  # Frank Green teaches in the Chemistry department

        # Insert into Semester
        semester_spring_2024 = Semester.objects.create(name='Spring 2024', academic_year=academic_year_2024)
        semester_fall_2024 = Semester.objects.create(name='Fall 2024', academic_year=academic_year_2024)
        semester_spring_2025 = Semester.objects.create(name='Spring 2025', academic_year=academic_year_2025)
        semester_fall_2023 = Semester.objects.create(name='Fall 2023', academic_year=academic_year_2023)

        # Insert into TeacherCourseSemester
        teacher_course_semester_1 = TeacherCourseSemester.objects.create(teacher=teacher_bob, course=course_cs101,
                                                                         semester=semester_spring_2024)
        teacher_course_semester_2 = TeacherCourseSemester.objects.create(teacher=teacher_charlie, course=course_math101,
                                                                         semester=semester_spring_2024)
        teacher_course_semester_3 = TeacherCourseSemester.objects.create(teacher=teacher_charlie, course=course_hist101,
                                                                         semester=semester_fall_2024)
        teacher_course_semester_4 = TeacherCourseSemester.objects.create(teacher=teacher_frank, course=course_chem101,
                                                                         semester=semester_fall_2023)

        # Insert into StudentTeacherCourseSemester
        StudentTeacherCourseSemester.objects.create(student=student_david,
                                                    teacher_course_semester=teacher_course_semester_1, grade='A',
                                                    status='Completed')
        StudentTeacherCourseSemester.objects.create(student=student_emma,
                                                    teacher_course_semester=teacher_course_semester_2, grade='B',
                                                    status='Completed')
        StudentTeacherCourseSemester.objects.create(student=student_grace,
                                                    teacher_course_semester=teacher_course_semester_3, grade='A',
                                                    status='Completed')
        StudentTeacherCourseSemester.objects.create(student=student_hannah,
                                                    teacher_course_semester=teacher_course_semester_4, grade='B',
                                                    status='Completed')

        print("Data inserted successfully!")
