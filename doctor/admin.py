from django.contrib import admin
from .models import Specialization, Designation, AvailableTime, Doctor, Review
# Register your models here.

class SpecializationAmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

class DesignationAmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Specialization, SpecializationAmin)
admin.site.register(Designation, DesignationAmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)