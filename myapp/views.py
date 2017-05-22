from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, render , redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forms import PollForm, AddForm
from .models import Poll, Add_act,Student

from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    student = Student.objects.all()
    print Activity
    print student
    return render(request, 'home.html', {'Activity': Activity, 'student': student })


username = ""
# def home(request):
#     Activity = Add_act.objects.all().order_by('-id')[:20]
#     student = Student.objects.all()
#     print Activity
#     print student
#     return render(request, 'home.html', {'Activity': Activity, 'student': student })

def activitylist(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'activitylist.html', {'Activity': Activity})

def category(request):
    return render(request, 'category.html')

def art(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'art.html', {'Activity': Activity})

def camp(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'camp.html', {'Activity': Activity })

def club(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'club.html', {'Activity': Activity})

def education(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'education.html', {'Activity': Activity})

def music(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'music.html', {'Activity': Activity})


def other(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'other.html', {'Activity': Activity})

def sport(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'sport.html', {'Activity': Activity })

def workshop(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    print Activity
    return render(request, 'workshop.html', {'Activity': Activity })

class CreateAddView(CreateView):
    queryset = Add_act()
    template_name='add.html'
    form_class = AddForm
    success_url = '/'
    def form_valid(self, form):
        return super(CreateAddView, self).form_valid(form)

class UpdateAddView(UpdateView):
    queryset = Add_act.objects.all()
    template_name='add.html'
    form_class = AddForm
    success_url = '/'

class ListAddView(ListView):
    model = Add_act
    template_name='add_list.html'

def voteScore(request, id=1):
    score = request.GET.get("day")
    activity = Add_act.objects.get(id=id);
    vote = Poll.objects.create(days=score)
    vote.user = username
    vote.activity = activity
    vote.save()
    print(score)
    return redirect('home')

def detail(request, id=1):
    activity = Add_act.objects.get(id=id);
    student = Student.objects.all()
    print activity
    print student
    return render(request, 'detail.html', {'activity': activity ,'id':id,'student': student})

def voteResult(request,id="1"):
    monday = 0;tuesday = 0; wednesday = 0; thursday = 0; friday = 0
    Activity = Add_act.objects.get(id=id);
    scoreResult = Poll.objects.filter(activity_id = id)
    dayStr=""


    for i in scoreResult:
        dayStr = str(i.days)+"s"
        if(dayStr == "Mondays"):
            monday+=1
        if(dayStr == "Tuesdays"):
            tuesday+=1
        if(dayStr == "Wednesdays"):
            wednesday+=1
        if(dayStr == "Thursdays"):
            thursday+=1
        if(dayStr == "Fridays"):
            friday+=1


    dayResult = [monday,tuesday,wednesday,thursday,friday]
    dayList = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    dayDic =  {"monday":monday, "tuesday":tuesday, "wednesday": wednesday, "thursday": thursday, "friday": friday}
    print(dayDic["monday"])
    return render(request, 'vote_result.html', {'activity': Activity, "dayList": dayList, "dayResult":dayResult})