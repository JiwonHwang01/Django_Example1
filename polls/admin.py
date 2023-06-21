from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date']})
    ]    
    inlines = [ChoiceInline]
    list_filter = ['pub_date'] # 생성날짜로 필터
    search_fields = ['question_text'] # 검색박스

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)