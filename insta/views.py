from django.shortcuts import render





def index(request):

    current_user = request.user
    images = Image.objects.all()
    users = Profile.objrcts.all()

    return render(request, 'all-posts/index.html', {"images":images})




def search(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        search_item = request.GET.get("article")
        searched_profile = Profile.search_by_profile(search_item)
        message = f"{search_item}"

        return render(request, 'all-posts/search.html',{message: message,"users": searched_profile})

    else:
        message = "You haven't searched for any profile"    
        return ender(request, 'all-posts/search.html', {message: message})



def new_comment(request,id):
    current_user = request.user

    image = Image.get_image_by_id(id)
    print(current_user)

    if request.method=='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = current_user
            comment.post = image
            comment.save()
            return redirect('welcome')

    else:
        form = CommentForm()
        return render(request,'all-posts/comment.html'{"form":form, "image":image})



