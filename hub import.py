import os, sys
import csv
proj_path = "/Users/tom/Desktop/New"
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
readtmp = "app/result/hubs.csv"
dataReader = csv.reader(open(readtmp), delimiter=',')

for row in dataReader:
    if row[0] != 'SITE': # Ignore the header row, import everything else
#        loc = Locations()

        hub = Hub()
        site = row[0]
        locid = Locations.objects.get(site__istartswith = site)
        hub.HUB_dns = row[1]
        hub.HUB_ip = row[2]
        hub.HUB_mask = row[3]
        hub.HUB_gate = row[4]
        hub.HUB_ntp = row[5]
        hub.HUB_sw = row[6]
        hub.locations = locid
        hub.save()
