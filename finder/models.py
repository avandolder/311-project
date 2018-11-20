from django.db import models

class CourseTime(models.Models):
    dates = models.CharField(max_length=3)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Professor(models.Models):
    name = models.CharFiel(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Course(models.Models):
    faculty = models.IntegerField()
    department = models.IntegerField()
    course = models.IntegerField()
    name = models.CharField(max_length=50)
    desc = models.TextField()
    review_amt = models.IntegerField()
    review_avg = models.FloatField(min=1.0, max=5.0)
