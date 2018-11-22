from django.contrib import admin

from .models import Course, CourseTime, Professor

admin.site.register(Course)
admin.site.register(CourseTime)
admin.site.register(Professor)
