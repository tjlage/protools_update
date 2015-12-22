import os, sys
import csv
proj_path = "/Users/tom/Desktop/projects"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from app.models import *

#txtreader = open("time.txt",'r')
readtmp = "app/result/ICR CSV.csv"
dataReader = csv.reader(open(readtmp), delimiter=',')

for row in dataReader:
    if row[0] != 'Site': # Ignore the header row, import everything else

        icr = ICR()
        site = row[0]
        locid = Locations.objects.get(site__istartswith = site)
        icr.tunnel = row[1]
        icr.sysType = row[2]
        icr.scale = row[3]
        icr.locations = locid

#        dtexists = Locations.objects.filter(site__startswith = site).exists()
#        diexists = ICR.objects.filter(tunnel__iexact = icr.tunnel).exists()

#        if dtexists and diexists:
#            pass
#        else:
        icr.save()
