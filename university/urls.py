from django.urls import path, include
from rest_framework.routers import DefaultRouter
from university.views import CourseViewSet, DepartmentViewSet, FeedbackViewSet, UserViewSet, TeacherCourseSemesterViewSet, RoleViewSet

router = DefaultRouter()

router.register(r'courses', CourseViewSet, basename='course')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'feedback', FeedbackViewSet, basename='feedback')
router.register(r'users', UserViewSet, basename='user')
router.register(r'teacher_courses', TeacherCourseSemesterViewSet, basename='teacher-course-semester')
router.register(r'roles', RoleViewSet, basename='role')

urlpatterns = [
    path('', include(router.urls)),
]