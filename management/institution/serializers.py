from rest_framework import serializers

from institution.models import Student, Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta():
        model = Course
        fields = ('id', 'year', 'division')


class StudentSerializer(serializers.ModelSerializer):

    class Meta():
        model = Student
        fields = ('id', 'name', 'last_name', 'dni',
                  'course', 'phone_number', 'address')
