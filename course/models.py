from django.db import models

# Create your models here.
from common.models import User

type = (
    ("free", "Free"),
    ("premium", "Premium")
)

level = (
    ('1', "beginner"),
    ('2', "intermediate"),
    ('3', "advanced"),
)

duration = (
    ('0-1', "0-1 Hour"),
    ('1-3', "1-3 Hour"),
    ('3+', "3+ Hour"),
)


class Author(models.Model):
    full_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=128)
    courses_count = models.PositiveIntegerField()



    def __str__(self):
        return self.full_name


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    image = models.ImageField(max_length=128)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name="courses")
    image = models.ImageField(upload_to='course/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='courses')
    tags = models.ManyToManyField(Tag, related_name='courses')

    level = models.CharField(max_length=128, choices=level)
    type = models.CharField(max_length=128, choices=type)
    duration = models.CharField(max_length=128, choices=duration)

    students_count = models.PositiveIntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title


class CourseUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user')

    enrolled_date = models.DateTimeField()
    course_completion_percentage = models.PositiveIntegerField()
