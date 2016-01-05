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
readtmp = "app/result/icr.csv"
dataReader = csv.reader(open(readtmp), delimiter=',')

for row in dataReader:
    if row[0] != 'Site': # Ignore the header row, import everything else

        icr = ICR()
        site = row[0]
        locid = Locations.objects.get(site__istartswith = site)
        icr.tunnel = row[1]
        icr.sysType = row[2]
        icr.peType = row[3]
        icr.msc = row[4]
        icr.icr2 = row[5]
        icr.icr3 = row[6]
        icr.led = row[7]
        icr.vms = row[8]
        icr.clv490 = row[9]
        icr.clv690 = row[10]
        icr.mirror = row[11]
        icr.clvstp = row[12]
        icr.sopas = row[13]
        icr.scale = row[14]
        icr.msc_ip1 = row[15]
        icr.msc_mask1 = row[16]
        icr.msc_gate1 = row[17]
        icr.msc_ip2 = row[18]
        icr.msc_mask2 = row[19]
        icr.msc_gate2 = row[20]
        icr.sntp_ip = row[21]
        icr.sspc_ip = row[22]
        icr.sspc_mask = row[23]
        icr.sspc_gate = row[24]
        icr.sspc_sntp = row[25]
        icr.hdd = row[26]
        icr.sspc_img = row[27]
        icr.sspc_sw = row[27]
        icr.locations = locid

#        dtexists = Locations.objects.filter(site__startswith = site).exists()
#        diexists = ICR.objects.filter(tunnel__iexact = icr.tunnel).exists()

#        if dtexists and diexists:
#            pass
#        else:
        icr.save()
