from django.contrib import admin
from .models import Resource, Method


class MethodLine(admin.StackedInline):
    model = Method
    extra = 2

class ResourceAdmin(admin.ModelAdmin):
    inlines = [MethodLine]


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Method)