from django.db import models

class Course(models.Model):
    faculty = models.IntegerField()
    department = models.IntegerField()
    course = models.IntegerField()
    name = models.CharField(max_length=50)
    desc = models.TextField()
    review_amt = models.IntegerField()
    review_avg = models.FloatField()

class CourseTime(models.Model):
    dates = models.CharField(max_length=3)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Professor(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
