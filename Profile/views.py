from django.shortcuts import render
from  .forms import PostForm,UserForm,ProfileForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
def post_new(request):
    form = PostForm()
    return render(request, 'Profile/post_form.html', {'form': form})

def user_new(request):
    form = UserForm()
    return render(request, 'Profile/user_form.html', {'form': form})

def profile_new(request):
    form = ProfileForm()
    return render(request, 'Profile/profile_form.html', {'form': form})