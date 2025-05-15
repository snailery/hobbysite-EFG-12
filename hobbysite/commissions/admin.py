from django.contrib import admin
from .models import Commission, Job, JobApplication


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    inlines = [JobInline]


class JobApplicationInline(admin.TabularInline):
    model = JobApplication


class JobAdmin(admin.ModelAdmin):
    inlines = [JobApplicationInline]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
