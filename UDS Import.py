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
readtmp = "app/result/UDS.csv"
dataReader = csv.reader(open(readtmp), delimiter=',')

for row in dataReader:
    if row[0] != 'Site': # Ignore the header row, import everything else

        uds = UDS()
        site = row[0]
        locid = Locations.objects.get(site__istartswith = site)
        uds.tunnel = row[1]
        uds.sysType = row[2]
        uds.vms = row[3]
        uds.msc = row[4]
        uds.clvstp = row[5]
        uds.mscfw = row[6]
        uds.altName = row[7]
        uds.msc_ip = row[8]
        uds.msc_mask = row[9]
        uds.msc_gate = row[10]
        uds.msc_sntp = row[11]
        uds.sspc_ip = row[12]
        uds.sspc_mask = row[13]
        uds.sspc_gate = row[14]
        uds.sspc_sntp = row[15]
        uds.locations = locid

        uds.save()
