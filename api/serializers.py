from rest_framework import serializers
from .models import *

# 1. Serializer for Org
class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = '__all__'

# 2. Serializer for Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# 3. Serializer for Semesters
class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'

# 4. Serializer for Subjects
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

# 5. Serializer for TechSkills
class TechSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSkills
        fields = '__all__'

# 6. Serializer for StudentTable
class StudentTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTable
        fields = '__all__'

# 7. Serializer for Assignments (used for POST/Create)
class AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = '__all__'

# 8. Serializer for AssignmentTransactionTable (used for POST/Create)
class AssignmentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTransactionTable
        fields = '__all__'


# 9. A special READ-ONLY serializer for the "Display" page
# This one nests related data to match your table
class AssignmentTransactionDisplaySerializer(serializers.ModelSerializer):
    # Get data from the related Student model
    student_usn_no = serializers.CharField(source='student.student_usn_no', read_only=True)
    # NOTE: Your "Student Table" model does not have a 'student_name' field.
    # The table shows 'student name'. I am using 'student_usn_no' instead.
    # If you add 'student_name' to your StudentTable model, you can add it here.
    
    # Get data from the related Assignment and its relations
    course = serializers.CharField(source='assignment.course.course_name', read_only=True)
    semester = serializers.CharField(source='assignment.semester.semester_name', read_only=True)
    subject = serializers.CharField(source='assignment.subject.subject_name', read_only=True)
    assignment_name = serializers.CharField(source='assignment.assignment_name', read_only=True)
    total_marks = serializers.IntegerField(source='assignment.total_marks', read_only=True)

    class Meta:
        model = AssignmentTransactionTable
        # List all the fields you want to display in your table
        fields = [
            'student_usn_no', 
            # 'student_name', # Add this if you update your model
            'course', 
            'semester', 
            'subject', 
            'assignment_name', 
            'total_marks', 
            'obtained_marks', 
            'candidate_submit_date', 
            'remarks'
        ]