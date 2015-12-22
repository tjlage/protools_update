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
readtmp = "app/result/maintence sample.csv"
dataReader = csv.reader(open(readtmp), delimiter=',')

for row in dataReader:
    if row[0] != 'Name': # Ignore the header row, import everything else
        loc = Locations()
        loc.division = row[0]
        loc.site = row[1]
        loc.street = row[6]
        loc.city = row[7]
        loc.state = row[8]
        loc.zzip = row[9]


        dtexists = Locations.objects.filter(site__iexact = loc.site).exists()

        if dtexists:
            pass
        else:
            loc.save()

#        con.locations = locations
#        con.save()
        locid = Locations.objects.latest('id')
        con = Contacts()
        con.contact = row[2]
        con.officeNum = row[3]
        con.faxNum = row[4]
        con.conCell = row[5]
        con.email = row[10]
        con.locations = locid
        con.save()
