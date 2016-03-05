from django.db import models

import string
import random


YEAR_CHOICES = (
    ('primero', 'Primero'),
    ('segundo', 'Segundo'),
    ('tercero', 'Tercero'),
)

DIVISION_CHOICES = (
    ('a', 'A'),
    ('b', 'B'),
    ('economia', 'Economia'),
    ('cs_naturales', 'Ciencias Naturales'),
)


def get_hash_id():
    """Generates random 16 char lowercase string with numbers and letters"""
    hash_seed = string.ascii_lowercase + string.digits
    hash_string = ''
    for x in random.sample(hash_seed, 16):
        hash_string += x
    return hash_string


class Course(models.Model):

    id = models.CharField(primary_key=True, default=get_hash_id,
                          max_length=16, editable=False)
    year = models.CharField(max_length=16, choices=YEAR_CHOICES)
    division = models.CharField(max_length=16, choices=DIVISION_CHOICES)

    def __unicode__(self):
        return '{} {}'.format(self.year.capitalize(),
                              self.division.capitalize())


class Student(models.Model):

    id = models.CharField(primary_key=True, default=get_hash_id,
                          max_length=16, editable=False)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dni = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=32, blank=True)
    course = models.ForeignKey(Course)


#class Planilla(models.Model):

#    id = models.CharField(primary_key=True, default=get_hash_id, max_length=16,
#                          editable=False)
#    date = models.DateField()
#    responsable = models.CharField(max_length=32)
#    course = models.ForeignKey(Course)
#    alumnos = JSONField()
