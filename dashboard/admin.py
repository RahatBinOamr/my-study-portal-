from django.contrib import admin
from .models import Notes,HomeWork,Todo

class NotesAdmin(admin.ModelAdmin):
  list_display = ('user','title','description')
admin.site.register(Notes,NotesAdmin)

class HomeworkAdmin(admin.ModelAdmin):
  list_display = ('user','title','description','due','is_finished')
admin.site.register(HomeWork,HomeworkAdmin)
class TodoAdmin(admin.ModelAdmin):
  list_display = ('user','title','is_finished')
admin.site.register(Todo,TodoAdmin)