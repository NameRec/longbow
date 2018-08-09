from django.contrib import admin
from .models import Test, Question, Answer

from adminsortable2.admin import SortableInlineAdminMixin

from django.utils.safestring import mark_safe
from django.urls import reverse


class EditLinkToInlineObject(object):

    @classmethod
    def edit_link(cls, instance):
        url = reverse(f'admin:{instance._meta.app_label}_{instance._meta.model_name}_change', args=[instance.pk])
        return mark_safe(f'<a href="{url}">edit</a>') if instance.pk else ''


class HiddenInAdminRoot:
    pass
    # def get_model_perms(self, request):
    #     return {}


class QuestionInline(EditLinkToInlineObject, SortableInlineAdminMixin, admin.TabularInline):
    model = Question
    readonly_fields = ('edit_link',)


class AnswerInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Answer


class AnswerAdmin(HiddenInAdminRoot, admin.ModelAdmin):
    pass


class QuestionAdmin(HiddenInAdminRoot, admin.ModelAdmin):
    inlines = [AnswerInline]


class TestAdmin(admin.ModelAdmin):
    list_display = ('description', 'pub_date')
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
