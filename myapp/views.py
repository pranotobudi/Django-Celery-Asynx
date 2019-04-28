from django.shortcuts import render
from .forms import GenerateUserForm
from .tasks import generate_user_task
from django.http import HttpResponse
import json
from celery.result import AsyncResult
from myapp.models import Photo
from django.views.generic.list import ListView


# Create your views here.
def home_view(request):
    return render(request, 'myapp/home.html')

# def generate_random_user_pull(request):
#     return render(request, 'myapp/generate_random_user_pull.html') 

def generate_random_user_push(request):
    pass 

def load_flickr_images_pull(request):
    pass

def load_flickr_images_push(request):
    pass

# Create your views here.
def generate_random_user_pull(request):
    if request.method == 'POST':
        #call task here
        print("||||||||||||||||||||||||||||||||||||||")
        #print("MASUK Views.py: get_task_info, task_id: ", task_id)
        form = GenerateUserForm(request.POST)
        if form.is_valid():
            total_user = form.cleaned_data.get('total_user_input')
            task = generate_user_task.delay(total_user)
            return HttpResponse(json.dumps({'task_id': task.id}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'task_id': None}), content_type='application/json')

        #return AsyncTask result
    else:
        #GET: return empty form for first time load
        form = GenerateUserForm()

    return render(request, 'myapp/generate_random_user_pull.html', {'form': form})
class PhotoView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    paginate_by = 24


def check_progress_view(request):
    task_id = request.GET.get('task_id', None)

    if task_id:
        task = AsyncResult(task_id)
        data = {
            'state': task.state,
            'result': task.result,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    return HttpResponse('No job id given.')
    
