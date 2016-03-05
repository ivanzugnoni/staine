from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
#from rest_framework.response import Response

from institution.models import Student, Course
from institution.serializers import StudentSerializer, CourseSerializer


class StudentViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    """
    This endpoint represents Exercises.

    ## Allowed actions:

    *   List all students:

        `GET /students`

    *   Retrieve one particular student:

        `GET /students/:id`
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def filter_queryset(self, queryset):
        queryset = super(StudentViewSet, self).filter_queryset(queryset)

        # filter students of one particular course
        course_id = self.request.query_params.get('course')
        if course_id:
            course = get_object_or_404(Course, id=course_id)
            queryset = queryset.filter(course=course)

        return queryset


class CourseViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    """
    This endpoint represents Exercises.

    ## Allowed actions:

    *   List all courses:

        `GET /courses`

    *   Retrieve one particular course:

        `GET /courses/:id`
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
