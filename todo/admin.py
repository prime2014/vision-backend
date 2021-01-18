from django.contrib import admin
from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('cat', 'employee', 'task',
                    'start_time', 'end_time', 'status')
    list_filter = ('cat', 'start_time', 'end_time')
    search_fields = ('employee', 'start_time')
    date_hierarchy = "start_time"
