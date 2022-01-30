from django.contrib import admin

from .models import Question, Choise

class ChoiseInLine(admin.TabularInline):
    model = Choise
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiseInLine]
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)


# Register your models here.
