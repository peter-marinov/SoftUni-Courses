from datetime import date

from django.db import models
from django.urls import reverse

from models_demos.web.validators import validate_in_the_past

# Create your models here.

# model fields == class attributes in Model classes

'''
PostgreSQL: varying char (30)
SQL Server: VARCHAR(30)
Other: CHARVAR(30) // only for demo
'''


# class EmployeeLevel(Emum):
#     JUNIOR = 'Junior'
#     REGULAR = 'Regular'
#     SENIOR = 'Senior'


class AuditInfoMixin(models.Model):
    class Meta:
        # 1. No table will be created in the DB
        # 2. Can be inherited in other models
        abstract = True

    # This will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    # This will be automatically set on each save / upload
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )


# class DeletableMixin(models.Model):
#     is_deleted = models.BooleanField(default=False)

class Department(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'Id {self.pk}; Name: {self.name}'

    def get_absolute_url(self):
        url = reverse('department details', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })

        return url


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(AuditInfoMixin, models.Model):
    class Meta:
        ordering = ('-years_of_experience', 'age',)

    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR)
    )
    # Var char(30) => string with max length 30
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level',
    )

    age = models.PositiveIntegerField(
        default=0,
    )

    # int
    years_of_experience = models.PositiveIntegerField()

    # Text = text with unlimited length
    review = models.TextField()

    start_date = models.DateField(
        validators=(validate_in_the_past,)
    )

    email = models.EmailField(
        # Adds UNIQUE constraint
        unique=True,
        # editable=False,
    )

    us_full_time = models.BooleanField(
        null=True,
    )

    # One-to-many
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    # Many-to-many
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def years_of_employment(self):
        return date.today() - self.start_date

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.full_name}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories Meta'

    name = models.CharField(
        max_length=15
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )


# Employee.objects.raw('SELECT * ') # SQL code into python
# Employee.objects.all() # Select *
# Employee.objects.create() # Insert
# Employee.objects.filter() # Select + Where
# Employee.objects.update() # Update


'''
Django ORM (Object-relational map)
'''


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )

    null = models.IntegerField(
        blank=False,
        null=True,
    )

    black_null = models.IntegerField(
        blank=True,
        null=False,
    )

    default = models.IntegerField(
        blank=False,
        null=False
    )


class EmployeesProject(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )
    # Additional info
