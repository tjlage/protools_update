from django.db import models
from django.utils import timezone

# Create your models here.

#class IP(models.Model):
#    date = models.CharField("Date", max_length=15)
#    ip = models.GenericIPAddressField("IP")
#    site = models.CharField("Site", max_length=50)
#    tunName = models.CharField("Tunnel Name", max_length=50)
#    tunType = models.CharField("Tunnel Type", max_length=3)
#    reach = models.CharField("Reachable", max_length=5)
#    disk = models.PositiveIntegerField("Disk Usage")
#    pe = models.PositiveIntegerField("PE Count")

#class Ping(models.Model):
    #reach = models.BooleanField(default=False)
    #created_date = models.DateTimeField(default=timezone.now)

class Locations(models.Model):
    site = models.CharField("Site", max_length=9, unique=True)
    division = models.CharField("Division", max_length=9)
    street = models.CharField("Street", max_length=60)
    city = models.CharField("City", max_length=25)
    state = models.CharField("State", max_length=15)
    zzip = models.CharField("Zip_Code", max_length=10)

class Contacts(models.Model):
    contact = models.CharField("Contact_Name", max_length=30)
    officeNum = models.CharField("Office_Number", max_length=25, null=True, blank=True)
    faxNum = models.CharField("Fax_Number", max_length=15, null=True, blank=True)
    conCell = models.CharField("Contact_Cell", max_length=15, null=True, blank=True)
    email = models.EmailField ("Email_Address", max_length=45, null=True, blank=True)
    locations = models.ForeignKey(Locations, to_field="site",on_delete=models.CASCADE)

class ICR(models.Model):
    tunnel = models.CharField("Tunnel", max_length=12)
    sysType = models.CharField("System_Type", max_length=4, null=True, blank=True)
    scale = models.CharField("Scale_Installed", max_length=4, null=True,blank=True)
    locations = models.ForeignKey(Locations, to_field="site",on_delete=models.CASCADE)
