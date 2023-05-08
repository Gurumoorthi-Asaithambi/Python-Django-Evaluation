from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .form import ImageForm
from django.db.models import Q
from .models import image

def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Already Exist")
                return redirect(register)
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login_user')

    else:
        print("This is not post method")
        return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            data = image.objects.all()
            context = {
              'data': data
             }
            return render(request, "showgallery.html", context)

        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('login_user')
    else:
        return render(request, "login.html")


def logout_user(request):
    auth.logout(request)
    return redirect("login_user")


def upload_image(request):

    data = image.objects.all()
    context = {
        'data': data
    }

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "showgallery.html", context)

    else:
        form = ImageForm()
    return render(request, 'imageupload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def display(request):
    data = image.objects.all()
    context = {
        'data': data
    }
    return render(request, "showgallery.html", context)


def SearchImage(request):
    query = request.GET.get('q')
    images = image.objects.filter(Q(image__icontains=query) | Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query))
    context = {
        'data': images
    }
    return render(request, "showgallery.html", context)
