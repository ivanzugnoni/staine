from django.contrib import admin

from .models import Student, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'course')
    search_fields = ('id', 'name', 'last_name')
    readonly_fields = ('id',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'division',)
    search_fields = ('id', 'year', 'division',)
    readonly_fields = ('id',)
