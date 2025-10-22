from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'teacher', 
        'get_student_name', 
        'teaching_score', 
        'punctuality_score', 
        'creation_date'
    )
    
    list_filter = ('teacher', 'creation_date')
    
    search_fields = (
        'teacher__user__first_name', 
        'teacher__user__last_name', 
        'student__username',
        'comment'
    )
    
    readonly_fields = ('teacher', 'student', 'creation_date')
    
    @admin.action(description='Student')
    def get_student_name(self, obj):
        if obj.student:
            return obj.student.username
        return "Anonymous"

admin.site.register(Review, ReviewAdmin)