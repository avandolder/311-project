from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView

from finder.models import Course

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/finder')
    else:
        form = UserCreationForm()
    return render(request, 'finder/signup.html', {'form':form})

def index(request):
    return render(request, 'finder/index.html', {})

def logout(request):
    django_logout(request)
    return redirect('/login')

def profile(request):
    return render(request, 'finder/profile.html')

def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        if not search_query:
            return render(request, 'finder/search.html')

        # Check if query is by name or code.
        if search_query.lstrip()[1].isdigit():
            # If the first character is numeric, then search by code.
            return redirect('/courseinfo/' + search_query.strip())
        else:
            courses = Course.objects.filter(name__icontains=search_query)
            print(courses)
            if len(courses) == 1:
                course = courses[0]
                course_code = f'{course.faculty}-{course.department}-{course.course}'
                return redirect('/courseinfo/' + course_code)

def faqs(request):
    return render(request, 'finder/faqs.html')

def paths(request):
    #return users saved paths
    return render(request, 'finder/paths.html')

def courseinfo(request, faculty, department, course):
    course = get_object_or_404(Course, faculty=faculty, department=department, course=course)
    return render(request, 'finder/courseinfo.html', {'course': course})
