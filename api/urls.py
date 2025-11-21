from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'orgs', views.OrgViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'semesters', views.SemestersViewSet)     # <-- Was SemesterViewSet
router.register(r'subjects', views.SubjectsViewSet)       # <-- New
router.register(r'techskills', views.TechSkillsViewSet)   # <-- New
router.register(r'students', views.StudentTableViewSet)   # <-- Was StudentViewSet
router.register(r'assignments', views.AssignmentsViewSet) # <-- Was AssignmentViewSet
router.register(r'transactions', views.AssignmentTransactionViewSet) # <-- New

urlpatterns = [
    path('', include(router.urls)),
]