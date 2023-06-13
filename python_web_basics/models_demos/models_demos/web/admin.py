from django.contrib import admin

# Register your models here.
from models_demos.web.models import Employee, NullBlankDemo, Department, Project, Category


# This model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level', 'department', 'department2')
    list_filter = ('level', 'department', 'first_name')
    search_fields = ('first_name', 'last_name')
    sortable_by = ('id', 'first_name')

    # fieldsets = (
    #     (
    #         'Personal info',
    #         {
    #             'fields': ('first_name', 'last_name', 'age')
    #         }
    #     ),
    #     (
    #         'Professional info',
    #         {
    #             'fields': ('level', 'years_of_experience')
    #         }
    #     ),
    #     (
    #         'Company info',
    #         {
    #             'fields': ('department', 'us_full_time', 'email', 'start_date',)
    #         }
    #     )
    # )

    def department2(self, obj):
        return obj.department.name

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
