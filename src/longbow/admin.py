from django.contrib import admin
from .models import Test, Question, Answer, TestPassing, TestPassingQuestion

from adminsortable2.admin import SortableInlineAdminMixin

from django.utils.safestring import mark_safe
from django.urls import reverse


class EditLinkToInlineObject(object):

    @classmethod
    def edit_link(cls, instance):
        url = reverse(f'admin:{instance._meta.app_label}_{instance._meta.model_name}_change', args=[instance.pk])
        return mark_safe(f'<a href="{url}">edit</a>') if instance.pk else ''


class HiddenInAdminRoot:
    """ Mixin to hide registered model in site admin interface """
    def get_model_perms(self, request):
        return {}


class QuestionInline(EditLinkToInlineObject, SortableInlineAdminMixin, admin.TabularInline):
    model = Question
    readonly_fields = ('edit_link',)


class AnswerInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Answer


@admin.register(Answer)
class AnswerAdmin(HiddenInAdminRoot, admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(HiddenInAdminRoot, admin.ModelAdmin):
    inlines = [AnswerInline]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('description', 'pub_date')
    inlines = [QuestionInline]


admin.site.register(TestPassing)
admin.site.register(TestPassingQuestion)