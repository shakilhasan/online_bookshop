from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

#..........
import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("test.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

#..........

def usignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()
        return redirect('book_home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})


def ulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_home')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')

def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/login')
