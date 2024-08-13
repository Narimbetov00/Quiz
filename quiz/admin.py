from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin
from django.contrib.admin import register,TabularInline

@register(Category)

class CategoryModelAdmin(SortableAdminMixin,admin.ModelAdmin):
    prepopulated_fields = {'slag':('title',)}

@register(Test)

class TestModelAdmin(SortableAdminMixin,admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}



class AnswerModelAdmin(TabularInline):
    model = Answer


@register(Questions)
class QuestionsModelAdmin(SortableAdminMixin,admin.ModelAdmin):
    inlines = (AnswerModelAdmin,)
