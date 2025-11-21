import uuid
from django.db import models

class Org(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=255, unique=True)
    course_code = models.CharField(max_length=50, unique=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, related_name='courses')

class Semesters(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    semester_name = models.CharField(max_length=100, unique=True)
    sem_code = models.CharField(max_length=50, unique=True)


class Subjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_name = models.CharField(max_length=255, unique=True)
    subject_code = models.CharField(max_length=50, unique=True)

class TechSkills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_name = models.CharField(max_length=100, unique=True)
    skill_code = models.CharField(max_length=50, unique=True)

class StudentTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_usn_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

class Assignments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assignment_name = models.CharField(max_length=255)
    assignment_description = models.TextField(max_length=500)
    start_date = models.DateTimeField()
    submission_end_date = models.DateTimeField()
    total_marks = models.IntegerField()
    assignment_code = models.CharField(max_length=50, unique=True)
    
    tech_skill = models.ForeignKey(TechSkills, on_delete=models.SET_NULL, null=True, related_name='assignments')
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, related_name='assignments')
    semester = models.ForeignKey(Semesters, on_delete=models.SET_NULL, null=True, related_name='assignments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')

class AssignmentTransactionTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    obtained_marks = models.IntegerField()
    candidate_submit_date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)
    
    student = models.ForeignKey(StudentTable, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE, related_name='submissions')