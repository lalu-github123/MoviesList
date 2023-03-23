from django.shortcuts import render,redirect
from .models import Movielist
from .form import UpdateForm

# Create your views here.
def home(request):
    movies = Movielist.objects.all()
    return render(request,"home.html",{'movies':movies})
def add_movies(request):
    if request.method=='POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        image = request.FILES['img']
        movie = Movielist(name=name,year=year,desc=desc,img=image)
        movie.save();
        return redirect('/')
    return render(request,"add.html")
def update(request,id):
    update_movie = Movielist.objects.get(id=id)
    form = UpdateForm(request.POST or None,request.FILES,instance=update_movie)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,"update.html",{'form':form})
def delete(request,id):
    if request.method=='POST':
        movie = Movielist.objects.get(id=id)
        movie.delete();
        return redirect('/')
    return render(request,"delete.html")
def show(request,id):
    movie = Movielist.objects.get(id=id)
    return render(request,"show.html",{'movie':movie})