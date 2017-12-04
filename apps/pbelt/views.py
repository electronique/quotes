from django.shortcuts import render, HttpResponse,redirect

from django.contrib import messages

from models import User
from models import Quote
from models import Favorite

# Create your views here.
def index(request):
    return render(request, "pbelt/index.html")

def reg(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/pbelt/reg')
    request.session['username'] = result.username
    messages.success(request, "Successfully registered!")
    return redirect('/pbelt')

def login(request):
    result = User.objects.validate_login(request.POST)
    values = request.POST
    request.session['username'] = request.POST['username']
    if type(result) == list:
        print result
        for err in result:
            print err
            if err == 'username/password incorrect':
                messages.error(request, err)
                return redirect('/pbelt')
            elif err =='username/password correct':
                messages.success(request, "Successfully logged in!")
                request.session['username'] = values['username']
        return redirect('/pbelt/allquotes')
def logout(request):
    request.session.clear()
    return redirect('/pbelt/')

def allquotes(request):
        request.session['username']
        loggeduser= User.objects.filter(username=request.session['username'])
        for u in loggeduser:
            print u.name
            print u.id
            context={
                'allquotes':Quote.objects.all(),
                'user': User.objects.get(id = u.id),
                'favorites':Favorite.objects.all()
            }
        return render(request,'pbelt/allquotes.html',context)
def addquote(request,id):
    if len(request.POST['quote'])>3:
        Quote.objects.create(name=request.POST['name'],quote=request.POST['quote'],user=User.objects.get(id=id))
        messages.success(request,"thanks for adding this quote!")
        return redirect('/pbelt/allquotes')
    else:
        messages.error(request,"Please add a quote")
        return redirect('/pbelt/allquotes')
def myfav(request,id,q):
    request.session['username']
    print q
    print id
    Favorite.objects.create(favoriteuser=User.objects.get(id=id),favoritequote=Quote.objects.get(id=q))
    return redirect('/pbelt/allquotes')
def myfavdelete(request,id):
    f = Favorite.objects.get(id=id)
    f.delete()  
    return redirect('/pbelt/allquotes')
def postview(request,id):
    request.session['username']
    context={
                'allquotes':Quote.objects.all(),
                'user': User.objects.get(id = id)
            }
    return render(request,'pbelt/postview.html',context)