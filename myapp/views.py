from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forms import PollForm, AddForm
from .models import Poll, Add_act

from django.shortcuts import render
# Create your views here.

def home(request):
    Activity = Add_act.objects.all().order_by('-id')[:20]
    Vote = Poll.objects.all()
    print Activity
    print Vote
    return render(request, 'home.html', {'Activity': Activity, 'Vote': Vote })

class CreateAddView(CreateView):
    queryset = Add_act()
    template_name='add_poll.html'
    form_class = AddForm
    success_url = '/'
    def form_valid(self, form):
        return super(CreateAddView, self).form_valid(form)

class UpdateAddView(UpdateView):
    queryset = Add_act.objects.all()
    template_name='add_poll.html'
    form_class = AddForm
    success_url = '/'

class ListAddView(ListView):
    model = Add_act
    template_name='add_poll_list.html'

def Vote(request,day="0"):
    Vote_objects = Poll.objects.all()
    score = request.GET.get('day')
    print day
    print score
    return render(request, 'vote.html', {'Vote_objects': Vote_objects,'Vote':day})