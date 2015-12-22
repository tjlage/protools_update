from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpRequest, HttpResponse
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count


def home(request):
#    ureachs = IP.objects.filter(reach = 'UNREACHABLE');
    return render_to_response('app/home.html')

def ping(request):
#    pings = IP.objects.all()
    return render_to_response('app/ping.html')

def sites(request):
    sites = Locations.objects.all()
    return render_to_response('app/sites.html', { 'sites' : sites })

def disk(request):
#    disks = IP.objects.all()
    return render_to_response('app/disk.html')

def pe(request):
#    pes = IP.objects.all()
    return render_to_response('app/pe.html')

def site_detail(request, pk):
    site = get_object_or_404(Locations, pk=pk)
    cons = Contacts.objects.filter(locations = site)
    return render(request, 'app/site_detail.html', {'site': site, 'cons': cons})
