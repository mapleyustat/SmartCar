from django.shortcuts import render
from team.models import Team
from django.db.models import ObjectDoesNotExist, Q

def index(request):
    s=request.GET.get('s')
    if s:
        team_list=Team.objects.filter(Q(name__contains=s) | Q(intro__contains=s)).order_by('-create_time')
        return render(request, 'team/search.html',{'s':s,'team_list':team_list})
    team_list=Team.objects.order_by('-create_time')
    return render(request, 'team/index.html',{'team_list':team_list})

def detail(request):
    pass

def create(request):
    pass

def edit(request):
    pass