from django.urls import path
from university.views import *

student_list = StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

student_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

teacher_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

teacher_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

semester_list = SemesterViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

semester_detail = SemesterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

student_teacher_course_semester_list = StudentTeacherCourseSemesterViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

student_teacher_course_semester_detail = StudentTeacherCourseSemesterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

course_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('teachers/', teacher_list, name='teacher-list'),
    path('teachers/<int:pk>/', teacher_detail, name='teacher-detail'),
    path('semesters/', semester_list, name='semester-list'),
    path('semesters/<int:pk>/', semester_detail, name='semester-detail'),
    path('student-teacher-course-semester/', student_teacher_course_semester_list, name='student-teacher-course-semester-list'),
    path('student-teacher-course-semester/<int:pk>/', student_teacher_course_semester_detail, name='student-teacher-course-semester-detail'),
    path('courses/', course_list, name='course-list'),
    path('courses/<int:pk>/', course_detail, name='course-detail'),
]
