from rest_framework import viewsets
from .models import *
from .serializers import *

# 1. ViewSet for Org
class OrgViewSet(viewsets.ModelViewSet):
    queryset = Org.objects.all()
    serializer_class = OrgSerializer

# 2. ViewSet for Course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 3. ViewSet for Semesters
class SemestersViewSet(viewsets.ModelViewSet):
    queryset = Semesters.objects.all()
    serializer_class = SemestersSerializer

# 4. ViewSet for Subjects
class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

# 5. ViewSet for TechSkills
class TechSkillsViewSet(viewsets.ModelViewSet):
    queryset = TechSkills.objects.all()
    serializer_class = TechSkillsSerializer

# 6. ViewSet for StudentTable
class StudentTableViewSet(viewsets.ModelViewSet):
    queryset = StudentTable.objects.all()
    serializer_class = StudentTableSerializer

# 7. ViewSet for Assignments (handles "Create Assignment")
class AssignmentsViewSet(viewsets.ModelViewSet):
    queryset = Assignments.objects.all()
    serializer_class = AssignmentsSerializer

# 8. ViewSet for AssignmentTransactionTable
class AssignmentTransactionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentTransactionTable.objects.all()

    # This function dynamically chooses the serializer
    def get_serializer_class(self):
        # For GET requests (list, retrieve), use the detailed display serializer
        if self.action == 'list' or self.action == 'retrieve':
            return AssignmentTransactionDisplaySerializer
        # For POST, PUT, PATCH (create, update), use the simple serializer
        return AssignmentTransactionSerializer
    
    # TODO: Add filtering logic here to support the filters in your image
    # You can filter the 'queryset' based on URL parameters like:
    # /api/transactions/?course=...&semester=...