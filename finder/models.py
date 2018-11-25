from django.db import models

class Course(models.Model):
    faculty = models.IntegerField()
    department = models.IntegerField()
    course = models.IntegerField()
    name = models.CharField(max_length=50)
    desc = models.TextField()
    review_amt = models.IntegerField()
    review_avg = models.FloatField()

    def __str__(self):
        return self.name

class CourseTime(models.Model):
    dates = models.CharField(max_length=3)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    semesters = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.name}: {self.semesters} {self.dates} {self.start_time}-{self.end_time}'

class Professor(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.name}: {self.name}'
