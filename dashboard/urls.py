from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.Home,name='home'),
    path('notes/' ,views.Note,name='notes'),
    path('notes_delete/<pk>' ,views.delete_note,name='delete_note'),
    path('notes_details/<pk>' ,views.note_details.as_view(),name='note-details'),
    path('notes_update/<pk>' ,views.update_note,name='note-update'),
    path('homework' , views.homeWork,name='home-work'),
    path('update_homework/<pk>' , views.update_homeWork,name='update_homework'),
    path('delete_homework/<pk>' , views.delete_homework,name='delete_homework'),
    path('youtube' , views.YouTube,name='youtube'),
    path('todo' , views.ToDo,name='todo'),
    path('update-todo/<pk>' , views.update_todo,name='update_todo'),
    path('delete-todo/<pk>' , views.delete_todo,name='delete_todo'),
    path('books' , views.Books,name='books'),
    
    path('wiki' , views.wiki,name='wiki'),
    
]


