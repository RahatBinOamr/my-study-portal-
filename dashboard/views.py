from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import generic
from .forms import *
from .models import *
from youtubesearchpython import VideosSearch
import requests
import wikipedia
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home(request):
  return render(request, 'dashboard/home.html')

@login_required
def Note(request):
  if request.method == 'POST':
    form = NotesForm(request.POST)
    if form.is_valid():
      notes = Notes(user=request.user, title= request.POST['title'] , description=request.POST['description'] )
      notes.save()
    messages.success(request,f"Notes saved successfully")

  form=NotesForm()
  notes= Notes.objects.filter(user= request.user)
  context={
    'notes': notes,
    'form': form
  }
  return render(request, 'dashboard/notes.html' , context)

@login_required
def delete_note(request,pk=None):
  Notes.objects.get(id=pk).delete()
  return redirect('notes')


class note_details(generic.DetailView):
  model = Notes
  

@login_required
def homeWork(request):
  if request.method=='POST':
    form = homeWorkForm(request.POST)
    if form.is_valid():
      try:
        isFinished = request.POST['is_finished']
        if isFinished =='on':
          isFinished=True
        else:
          isFinished=False
      except:
        isFinished=False

      homework=HomeWork(
        user=request.user , 
        title=request.POST['title'],
        subject=request.POST['subject'],
        description=request.POST['description'],
        due=request.POST['due'] , 
        is_finished=isFinished
        )
      homework.save()
    messages.success(request,f"homework save form successfully")
  else:
    form=homeWorkForm()
  homeworks= HomeWork.objects.filter(user=request.user)
  if len(homeworks) == 0:
    homework_done =True
  else:
    homework_done = False
  context={
    'homeworks': homeworks,
    'homework_done':homework_done,
    'form': form
  }
  return render(request, 'dashboard/homework.html',context)

@login_required
def update_homeWork(request,pk=None):
  homework = HomeWork.objects.get(id=pk)
  if homework.is_finished == True:
    homework.is_finished = False
  else:
    homework.is_finished = True
  homework.save() 
  return redirect('home-work')


@login_required
def delete_homework(request,pk=None):
  HomeWork.objects.get(id=pk).delete()
  return redirect('home-work')

@login_required
def YouTube(request):
  if request.method =="POST":
    form= DashboardForm()
    text=request.POST['text']
    videosSearch = VideosSearch(text,limit = 10)
    result_list=[]
    for i in videosSearch.result()['result']:
      result_dict={
        'input':text,
        'title':i['title'],
        'duration':i['duration'],
        'thumbnail':i['thumbnails'][0]['url'],
        'channel':i['channel']['name'],
        'link':i['link'],
        'views':i['viewCount']['short'],
        'published':i['publishedTime'],
      }
      descr=''
      if i['descriptionSnippet']:
        for j in i['descriptionSnippet']:
          descr+=j['text']
      result_dict['description']=descr
      result_list.append(result_dict)
      context={
        'form':form,
        'results':result_list,
        }
    return render(request, 'dashboard/youtube.html',context)
  else: 
    form= DashboardForm()
  context={
    'form':form,
    
  }
  return render(request, 'dashboard/youtube.html',context)


@login_required
def ToDo(request):
  try:
        isFinished = request.POST['is_finished']
        if isFinished =='on':
          isFinished=True
        else:
          isFinished=False
  except:
        isFinished=False
  if request.method == 'POST':
    form= TodoForm(request.POST)
    if form.is_valid():
      todos=Todo(
        user=request.user, 
        title= request.POST['title'],
        is_finished=isFinished
        )
      todos.save()
    messages.success(request,f"todo save form successfully")
  else:
    form= TodoForm()
  
  todo=Todo.objects.filter(user=request.user)
  if len(todo) == 0:
    todo_done =True
  else:
   todo_done = False
  context={
    'todo':todo,
    'form':form,
    'todo_done':todo_done,
  }
  return render(request, 'dashboard/todo.html',context)

@login_required
def update_todo(request,pk=None):
  todo = Todo.objects.get(id=pk)
  if todo.is_finished == True:
    todo.is_finished = False
  else:
    todo.is_finished = True
  todo.save() 
  return redirect('todo')

@login_required
def delete_todo(request,pk=None):
  Todo.objects.get(id=pk).delete()
  return redirect('todo')

@login_required
def Books(request):
  if request.method =="POST":
    form= DashboardForm()
    text=request.POST['text']
    url='https://www.googleapis.com/books/v1/volumes?q='+text
    r=requests.get(url)
    answer=r.json()
    result_list=[]
    for i in range(10):
      result_dict={
        'input':text,
        'title':answer['items'][i]['volumeInfo']['title'],
        'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
        'description':answer['items'][i]['volumeInfo'].get('description'),
        'count':answer['items'][i]['volumeInfo'].get('pageCount'),
        'categories':answer['items'][i]['volumeInfo'].get('categories'),
        'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
        'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
        'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
        
        
      }

      result_list.append(result_dict)
      context={
        'form':form,
        'results':result_list,
        }
    return render(request, 'dashboard/books.html',context)
  else: 
    form= DashboardForm()
    context={
    'form':form,
    }
  return render(request,'dashboard/books.html',context)



@login_required  
def wiki(request):
  if request.method == 'POST':
    text= request.POST['text']
    form= DashboardForm(request.POST)
    search=wikipedia.page(text)
    context={
      'form': form,
      'title':search.title,
      'link':search.url,
      'details':search.summary
    }
    return render(request, 'dashboard/wiki.html',context)
  else:
    form= DashboardForm()
    context={
      'form':form
    }
  return render(request, 'dashboard/wiki.html',context)



def Register(request):
  if request.method == 'POST':
    form = userRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,f"User registration successful")
      return redirect('login')
  else:
      form=userRegistrationForm()
  context={
    'form':form
  }
  return render(request, 'dashboard/register.html',context)