from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404
from .models import Image,Profile,Comments,Follow
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm,NewImageForm,commentForm
from django.contrib.auth.models import User
# Create your views here.





@login_required(login_url='/accounts/login/')
def welcome(request):
    all_images = Image.get_all_images()
    insta_users = Profile.get_all_instagram_users()
    current_user = request.user
    myprof = Profile.objects.filter(id = current_user.id).first()
    mycomm = Comments.objects.filter(id = current_user.id).first()
    return render(request, 'welcome.html', {"all_images":all_images, "insta_users":insta_users, "myprof":myprof, "mycomm":mycomm})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

   
@login_required(login_url='/accounts/login/')
def my_profile(request):

    current_user = request.user
    profi_images = Image.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"profi_images":profi_images, "my_profile":my_profile})

@login_required(login_url='/accounts/login/')
def search_users(request):
  if 'username' in request.GET and request.GET["username"]:
      search_term = request.GET.get("username")
      searched_users = Profile.search_by_profile(search_term)
      message = f"{search_term}"
      return render(request, "search.html",{"message":message,"users": searched_users})
  else:
      message = "You haven't searched for any term"
      return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_image(request):

    current_user = request.user
    user_images = Profile.objects.filter(user = current_user).first()
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = user_images
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'upload.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_comment(request, image_id):
    current_user = request.user
    image_item = Image.objects.filter(id = image_id).first()
    profiless = Profile.objects.filter( user = current_user.id).first()
    if request.method == 'POST':
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = profiless
            comment.commented_image = image_item
            comment.save()
            return redirect('welcome')

    else:
        form = commentForm()
    return render(request, 'comment_form.html', {"form": form, "image_id": image_id})


def likes(request,id):
   likes=0
   image = Image.objects.get(id=id)
   image.likes = image.likes+1
   image.save()
   return redirect("/")

@login_required(login_url='/accounts/login/')
def others_profile(request, ima_id):

    current_user = User.objects.filter(id = ima_id).first()
    profiless_images = Image.objects.filter(user = current_user)
    my_profiless = Profile.objects.filter(user = current_user).first()
    return render(request, 'other_usersprofile.html', {"profiless_images":profiless_images, "my_profiless":my_profiless})

@login_required(login_url='/accounts/login/')
def following(request, profile_id):
    current_user = request.user
    profile_user = Profile.objects.filter(id = profile_id).first()
    followers = Follow(from_user = current_user,profile = profile_user)
    followers.save()
    return redirect('othersprofile', profile_id)